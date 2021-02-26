import numpy as np
from matplotlib import pyplot as plt
import cv2

# I = cv2.imread('masoleh_gray.jpg', cv2.IMREAD_UNCHANGED)
# print(I.shape)
# print(I.dtype)
# print(type(I))
# print(I[10, 20])
# cv2.imshow('Masoleh Village', I)
# cv2.waitKey(1000)  # display the image for 10 seconds
# cv2.destroyAllWindows()
# I = cv2.imread('masoleh.jpg')
# print(I.shape)
# print(I.dtype)

# I = cv2.imread('masoleh.jpg', cv2.IMREAD_UNCHANGED)
# print(I.shape)
# print(I.dtype)
# I = cv2.imread('masoleh.jpg')
# print(I.shape)
# print(I.dtype)
# print(I[10, 20])
# cv2.imshow('Masoleh', I)
# cv2.waitKey(10000) # display the image for 10 seconds
# cv2.destroyAllWindows()


# plt.imshow(I[:, :, ::-1])
# plt.show()


# I = cv2.imread('masoleh.jpg', cv2.IMREAD_UNCHANGED)
# I[:,:,1] = 0
# plt.imshow(I[:,:,::-1])
# plt.show()
# cv2.imwrite('masoleh_nogreen.jpg', I)


# I = cv2.imread('damavand.jpg')
# J = cv2.imread('eram.jpg')
# print(I.shape)
# print(J.shape)
# K = I.copy()
# # K[::2,::2,:] = J[::2,::2,:]
# K = I//2+J//2
# cv2.imshow("Image 1", I)
# cv2.imshow("Image 2", J)
# cv2.imshow("Blending", K)
# cv2.waitKey(8000)
# cv2.destroyAllWindows()

# a = np.array([1,2,3,4,5,6,7,8,9,10], dtype=np.uint8)
# print(a)
# b = np.full((10,), 250, dtype=np.uint8)
# print(b)
# x = a + b
# print(x)
# print(cv2.add(a, b))

