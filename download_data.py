import PIL
from scipy.ndimage import imread
import numpy as np
import os

files = None
cwd = os.getcwd()
myPath = cwd + '/411a3/test_mini/'
files = os.listdir(myPath)
if(len(files) == 0):
	raise ValueError('There were no pictures to be read')

file = files[0]
x = imread(myPath + file, flatten=False, mode='RGB')
imageL = x.shape[0]
imageW = x.shape[1]
numImages = len(files)
data = np.zeros((numImages, imageL, imageW, 3))		# Channels = 3

for i in range(0, numImages):
	fileName = files[i]
	x = imread(myPath + fileName, flatten=False, mode='RGB')	# returns ndarray (L x W x 3)
	data[i,:,:,:] = x

np.save('test_mini_data', data)
	