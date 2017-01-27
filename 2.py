import matplotlib.pyplot as plt
import numpy as np

img=plt.imread('t2.jpg')

a=img.shape[1]>img.shape[0]
if(a):
    extra=img.shape[1]-img.shape[0]
print(a)
print(img.shape[1],img.shape[0])
print(extra)