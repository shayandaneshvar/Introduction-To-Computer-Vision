import matplotlib.pyplot as plt
import numpy as np
from imageio import imread

image = np.array(imread('masoleh_gray.jpg'))
reverse = np.array(image.copy())
reverse = reverse[-1::-1, ]
image = np.concatenate((image, reverse))
plt.imshow(image, cmap='gray')
plt.show()
