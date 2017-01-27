import matplotlib.pyplot as plt
import numpy as np

img=plt.imread('t2.jpg')


def plot_image(img):
    plt.imshow(img)
    plt.show()


a=img.shape[1]>img.shape[0]
if(a):
    extra=(img.shape[1]-img.shape[0])
    if(extra %2==0):
        crop = img[:, extra // 2:-extra // 2]
    else:
        crop = img[:, max(0, extra // 2 + 1):min(-1, -(extra // 2))]


print(a)
print(img.shape[1],img.shape[0])
print(extra)
print(extra %2==0)
print(-extra // 2)
print(max(0, extra // 2 + 1))
print(min(-1, -(extra // 2)))
plot_image(img[:,0:50])
