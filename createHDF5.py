from random import shuffle
import glob
import matplotlib.pyplot as plt
import matplotlib._png as png
import h5py
import numpy as np
shuffle_data = True  # shuffle the addresses before saving
hdf5_path = '/home/mak/Desktop/Stroboscopy/dataset1.hdf5'  # address to where you want to save the hdf5 file
train_path = '/home/mak/Desktop/Stroboscopy/AllImages/*.png'
# read addresses and labels from the 'train' folder
addrs = glob.glob(train_path)
# to shuffle data


train_addrs = addrs
hdf5_file = h5py.File(hdf5_path, mode='w')
train_shape = (len(train_addrs), 576, 720, 3)
hdf5_file.create_dataset("train_img", train_shape, np.uint8)

for i in range(len(train_addrs)):
    # print how many images are saved every 1000 images
    if i % 100 == 0 and i > 1:
        print 'Train data: {}/{}'.format(i, len(train_addrs))
    # read an image and resize to (224, 224)
    # cv2 load images as BGR, convert it to RGB
    addr = train_addrs[i]
    img =  png.read_png_int(addr)
    print img.dtype
    # add any image pre-processing here
    # if the data order is Theano, axis orders should change
    hdf5_file["train_img"][i,:,:,:] = img
#
hdf5_file.close()