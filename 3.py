from scipy.misc import imresize
import matplotlib.pyplot as plt
import numpy as np
img = plt.imread('t2.jpg')
data = np.concatenate([img_i[np.newaxis] for img_i in img], axis=0)
print(data)
plt.imshow(data)
plt.show()