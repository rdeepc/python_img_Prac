import sys
import matplotlib.pyplot as plt
import numpy as np
import os

# //filename=sys.argv[1]
filename='1.jpg'

cutImg=[]

def parts(highest,number):
    fraction=highest/number
    start=0
    result= []
    while start<highest:
        start=start+fraction
        result.append(start)
    return result
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


img=plt.imread(filename)
width_img=img.shape[1]
height_img=img.shape[0]

if height_img>width_img:
    x_lines=parts(width_img,3)
    y_lines=parts(height_img,4)
elif height_img<width_img:
    x_lines = parts(width_img,4)
    y_lines = parts(height_img,3)
else:
    x_lines = parts(width_img,3)
    y_lines = parts(height_img,3)
y_first_cut=0
y_first_cut_gap=y_lines[0]

for y in range(len(y_lines)):
    y_secondcut=int(y_first_cut+y_first_cut_gap)
    row_cut = plt.imshow(img[y_first_cut:y_secondcut,0:width_img], cmap=plt.get_cmap('gray'))
    x_first_cut = 0
    x_first_cut_gap = x_lines[0]
    for x in range(len(x_lines)):
        x_secondcut = int(x_first_cut + x_first_cut_gap)
        col_cut = plt.imshow(img[y_first_cut:y_secondcut, x_first_cut:x_secondcut], cmap=plt.get_cmap('gray'))
        x_first_cut = int(x_secondcut)
        plt.show()

    print(y_first_cut, y_secondcut)
    y_first_cut=int(y_secondcut)

    # plt.imshow(img[first_cut:secondcut,0:height_img], cmap=plt.get_cmap('gray'))
    # plt.show()
# for y in range(len(y_lines)):
#     plt.plot([0, width_img], [y_lines[y], y_lines[y]])

# gimg=rgb2gray(img)
# imgf=plt.imshow(img,cmap = plt.get_cmap('gray'))
# directory='c'
# if not os.path.exists(directory):
#     os.makedirs(directory)
# plt.imsave(directory+"/"+"s2.png",gimg,cmap = plt.get_cmap('gray'))
# plt.show()