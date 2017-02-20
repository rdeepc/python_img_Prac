import matplotlib.pyplot as plt
import numpy as np
import os.path as path
import os
import glob2
from random import randint

totalImg=[]
avgHeight=0;
avgWeight=0
source_directory = 'source'
destination='dataset'

working_num=str(3)
total_des_path=path.join(destination,working_num)
total_src_path=path.join(source_directory,working_num)


def collect_img(directory):
    image_list = []
    imgExt = ("png", "jpg", "jpeg")
    for filename in glob2.glob(directory+'/**/*.*'):  # assuming gif
        if ((path.splitext(filename)[1][1:]) in imgExt):
            img = plt.imread(filename)
            image_list.append(img)
    return image_list

def creatfolder(sub):
    if not os.path.exists(sub):
        os.makedirs(destination+'/'+sub)


creatfolder(working_num)


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


def collect_img(directory):
    image_list = []
    imgExt = ("png", "jpg", "jpeg")
    for filename in glob2.glob(directory+'/**/*.*'):  # assuming gif
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
    return result


folderN =0
def imgCutf(Singleimg,folderN):
    img=Singleimg
    imgCutColl = []
    width_img = img.shape[1]
    height_img = img.shape[0]

    if height_img > width_img:
        x_lines = parts(width_img, 3)
        y_lines = parts(height_img, 4)
    elif height_img < width_img:
        x_lines = parts(width_img, 4)
        y_lines = parts(height_img, 3)
    else:
        x_lines = parts(width_img, 3)
        y_lines = parts(height_img, 3)

    y_first_cut = 0
    y_first_cut_gap = y_lines[0]


    for y in range(len(y_lines)):
        # fn =(int)working_num
        y_secondcut = int(y_first_cut + y_first_cut_gap)
        row_cut = plt.imshow(img[y_first_cut:y_secondcut, 0:width_img])
        x_first_cut = 0
        x_first_cut_gap = x_lines[0]
        for x in range(len(x_lines)):
            x_secondcut = int(x_first_cut + x_first_cut_gap)
            # col_cut = plt.imshow(img[y_first_cut:y_secondcut, x_first_cut:x_secondcut])
            # creatfolder(str(fn))
            folderN = folderN + 1
            fileName="%d.jpg"%(folderN)
            fullName=total_des_path+"/"+str(fileName)
            plt.imsave(fullName,img[y_first_cut:y_secondcut, x_first_cut:x_secondcut])
            # imgCutColl.append(col_cut)
            # totalImg.append(col_cut)
            x_first_cut = int(x_secondcut)
            # fn = fn + 1
            # print(fileName)
            # folderN=folderN+1
            # print(fullName)
            # plt.show()

        # print(y_first_cut, y_secondcut)

        y_first_cut = int(y_secondcut)

    # return imgCutColl;
    return folderN

col1=collect_img(total_src_path)

incer=1;
for ic in col1:
    imgCutf(ic,folderN)
    folderN=12*incer
    incer=incer+1


