import numpy as np
import matplotlib.pyplot as plt

def parts(highest,number):
    fraction=highest/number
    start=0
    result= []
    while start<highest:
        start=start+fraction
        result.append(start)
    result.pop()
    return result


width_img=1654
height_img=2339
img = np.zeros([height_img,width_img,3],dtype=np.uint8)
img.fill(255)
print(parts(height_img,4))
plt.imshow(img)
plt.show()

# width_parts=width_img//3
# x = np.arange(0,width_img)
# y=np.split(x,width_img)
# print(y)

