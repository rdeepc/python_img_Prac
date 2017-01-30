# python 5.py image.png

import sys
import matplotlib.pyplot as plt
import numpy as np

filename=sys.argv[1]


def parts(highest,number):
    fraction=highest/number
    start=0
    result= []
    while start<highest:
        start=start+fraction
        result.append(start)
    result.pop()
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

for x in range(len(x_lines)):
    plt.plot([x_lines[x],x_lines[x]],[0,height_img])

for y in range(len(y_lines)):
    plt.plot([0, width_img], [y_lines[y], y_lines[y]])

plt.imshow(rgb2gray(img),cmap = plt.get_cmap('gray'))
plt.show()
# plt.imsave("s1.png",rgb2gray(img),cmap = plt.get_cmap('gray'))
# directory='c'
# if not os.path.exists(directory):
#     os.makedirs(directory)
# plt.imsave(directory+"/"+"s2.png",gimg,cmap = plt.get_cmap('gray'))
