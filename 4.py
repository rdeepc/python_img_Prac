import numpy as np
import matplotlib.pyplot as plt

width_img=1654
height_img=2339
img = np.zeros([height_img,width_img,3],dtype=np.uint8)
img.fill(255)
plt.imshow(img)
plt.show()