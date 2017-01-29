import numpy as np
import matplotlib.pyplot as plt
row_y=2
col_x=3
img = np.zeros([row_y,col_x,3], dtype=np.uint8)
img[0][0][0]=0
img[0][0][1]=40
img[0][0][2]=80
img[0][1][0]=200
img[0][1][1]=30
img[0][1][2]=50
img[0][2][0]=153
img[0][2][1]=242
img[0][2][2]=100
img[0][0][0]=63
img[0][0][1]=42
img[0][0][2]=80
img[0][1][0]=40
img[0][1][1]=10
img[0][1][2]=0
img[1][1][0]=200
img[1][1][1]=100
img[1][1][2]=0
img[0][2][0]=153
img[0][2][1]=242
img[0][2][2]=153
img[1][0][0]=153
img[1][0][1]=242
img[1][0][2]=40
img[1][2][0]=153
img[1][2][1]=242
img[1][2][2]=40





print(img)
plt.imshow(img)
plt.show()