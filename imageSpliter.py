import matplotlib.pyplot as plt
import numpy as np
import os.path as path
import glob2


def collect_img(directory):
    image_list = []
    imgExt = ("png", "jpg", "jpeg")
    for filename in glob2.glob(directory+'/*/**.*'):  # assuming gif
        if ((path.splitext(filename)[1][1:]) in imgExt):
            img = plt.imread(filename)
            image_list.append(img)
    return image_list


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


