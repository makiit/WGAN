import h5py
import numpy as np
import matplotlib.pyplot as plt
hdf5_path = '/home/mak/Desktop/Stroboscopy/dataset1.hdf5'
path2 = '/home/mak/Desktop/Generative Models/CartoonWGAN/dataset.hdf5'
hdf5_file = h5py.File(hdf5_path, "r")
# subtract the training mean
data_num = hdf5_file["train_img"].shape[0]
print data_num
images = hdf5_file["train_img"][0:10,:,:,:]
print images.dtype
img = images[0]
print img[0:10,0:10,0]