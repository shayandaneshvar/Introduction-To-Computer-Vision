import cv2
import numpy as np

I = cv2.imread('isfahan.jpg').astype(np.float32) / 255

size = 9  # bilateral filter size (diameter)
sigma_color = 0.2
sigma_space = 30

Jl = cv2.bilateralFilter(I, size, sigma_color, sigma_space)

cv2.imshow('original', I)
cv2.waitKey()

cv2.imshow('blurred_Gaussian', Jl)
cv2.waitKey()

cv2.destroyAllWindows()
