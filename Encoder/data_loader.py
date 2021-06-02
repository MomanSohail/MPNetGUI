import numpy as np


def load_dataset(dataset_path, dimension, N=30000, NP=1800):
    obs_size = 2800 if dimension == 2 else 6000
    obstacles = np.zeros((N, obs_size), dtype=np.float32)
    for i in range(4, N):
        temp = np.fromfile(dataset_path+'/obs_cloud/obc' + str(i) + '.dat')
        temp = temp.reshape(len(temp) // dimension, dimension)
        obstacles[i] = temp.flatten()

    print(obstacles.shape)
    return obstacles
