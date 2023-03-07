import numpy as np
import os

if __name__ == "__main__":
    PEMS03 = os.path.join('../','STSGCN_data/PEMS03/PEMS03.npz')
    PEMS03_Data = np.load(PEMS03)
    print(PEMS03_Data['data'])
    print(PEMS03_Data['data'].shape)
