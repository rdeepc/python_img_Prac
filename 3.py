import numpy as np
import matplotlib.pyplot as plt
row_y=2
col_x=3
img = np.zeros([row_y,col_x], dtype=np.uint8)
img[0][0]=255
img[0][1]=242
img[0][2]=0
img[1][0]=255
img[1][1]=0
img[1][2]=0


print(img)
plt.imshow(img)
plt.show()