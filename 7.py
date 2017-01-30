import matplotlib.pyplot as plt
import os.path as path
import glob2
image_list = []
imgExt = ("png","jpg","jpeg")
for filename in glob2.glob('ds/*/**.*'): #assuming gif
    if((path.splitext(filename)[1][1:]) in imgExt):
        img=plt.imread(filename)
        image_list.append(img)

print(image_list)


