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
x_lines=parts(width_img,3)
y_lines=parts(height_img,4)

for x in range(len(x_lines)):
    plt.plot([x_lines[x],x_lines[x]],[0,height_img])

for y in range(len(y_lines)):
    plt.plot([0, width_img], [y_lines[y], y_lines[y]])

plt.imshow(img)
plt.show()

# width_parts=width_img//3
# x = np.arange(0,width_img)
# y=np.split(x,width_img)
# print(y)

