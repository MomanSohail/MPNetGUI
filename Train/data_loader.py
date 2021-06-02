import torch
import os
import numpy as np
import os.path
import random
from torch.autograd import Variable
import torch.nn as nn


# Environment Encoder
class Encoder(nn.Module):
    def __init__(self, dimension):
        size = 2800 if dimension == 2 else 6000
        super(Encoder, self).__init__()
        self.encoder = nn.Sequential(nn.Linear(size, 512), nn.PReLU(), nn.Linear(512, 256), nn.PReLU(),
                                     nn.Linear(256, 128), nn.PReLU(), nn.Linear(128, 28))

    def forward(self, x):
        x = self.encoder(x)
        return x


# N=number of environments; NP=Number of Paths
def load_dataset(dataset_path, dimension, number_of_environments=100, number_of_paths=4000):  # N=100, NP=4000
    Q = Encoder()
    if dimension == 2:
        path = 'Models/encoders/2D/cae_encoder.pkl'
    else:
        path = 'Models/encoders/3D/cae_encoder.pkl'
    Q.load_state_dict(torch.load(path))
    if torch.cuda.is_available():
        Q.cuda()

    obs_rep = np.zeros((number_of_environments, 28), dtype=np.float32)
    for i in range(0, number_of_environments):
        temp = np.fromfile(dataset_path + '/obs_cloud/obc' + str(i) + '.dat')
        temp = temp.reshape(len(temp) // dimension, dimension)
        obs_size = 2800 if dimension == 2 else 6000
        obstacles = np.zeros((1, obs_size), dtype=np.float32)
        obstacles[0] = temp.flatten()
        inp = torch.from_numpy(obstacles)
        inp = Variable(inp).cuda()
        output = Q(inp)
        output = output.data.cpu()
        obs_rep[i] = output.numpy()

    # calculating length of the longest trajectory
    max_length = 0
    path_lengths = np.zeros((number_of_environments, number_of_paths), dtype=np.int8)
    for i in range(0, number_of_environments):
        for j in range(0, number_of_paths):
            file_name = dataset_path + '/e' + str(i) + '/path' + str(j) + '.dat'
            if os.path.isfile(file_name):
                path = np.fromfile(file_name)
                path = path.reshape(len(path) // dimension, dimension)
                path_lengths[i][j] = len(path)
                if len(path) > max_length:
                    max_length = len(path)

    paths = np.zeros((number_of_environments, number_of_paths, max_length, dimension), dtype=np.float32)  ## padded paths

    for i in range(0, number_of_environments):
        for j in range(0, number_of_paths):
            file_name = dataset_path + '/e' + str(i) + '/path' + str(j) + '.dat'
            if os.path.isfile(file_name):
                path = np.fromfile(file_name)
                path = path.reshape(len(path) // dimension, dimension)
                for k in range(0, len(path)):
                    paths[i][j][k] = path[k]
    dataset = []
    targets = []
    for i in range(0, number_of_environments):
        for j in range(0, number_of_paths):
            if path_lengths[i][j] > 0:
                for m in range(0, path_lengths[i][j] - 1):
                    data = np.zeros(28+2*dimension, dtype=np.float32)
                    for k in range(0, 28):
                        data[k] = obs_rep[i][k]
                    if dimension == 3:
                        data[28] = paths[i][j][m][0]
                        data[29] = paths[i][j][m][1]
                        data[30] = paths[i][j][m][2]
                        data[31] = paths[i][j][path_lengths[i][j] - 1][0]
                        data[32] = paths[i][j][path_lengths[i][j] - 1][1]
                        data[33] = paths[i][j][path_lengths[i][j] - 1][2]
                    else:
                        data[28] = paths[i][j][m][0]
                        data[29] = paths[i][j][m][1]
                        data[30] = paths[i][j][path_lengths[i][j] - 1][0]
                        data[31] = paths[i][j][path_lengths[i][j] - 1][1]
                    targets.append(paths[i][j][m + 1])
                    dataset.append(data)

    data = list(zip(dataset, targets))
    random.shuffle(data);
    # print("data = ", data)
    dataset, targets = zip(*data)
    return np.asarray(dataset), np.asarray(targets)
