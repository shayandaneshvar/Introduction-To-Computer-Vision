import cv2
import numpy as np

I = cv2.imread('karimi.jpg')

t = np.array([[0],
              [0]], dtype=np.float32)
A = np.array([[1, 0],
              [0, 1]], dtype=np.float32)

M = np.hstack([A, t])

# perspective effect
p = np.array([[-0.002, 0, 1]])

H = np.vstack([M,
               p])

output_size = (I.shape[1], I.shape[0])
J = cv2.warpPerspective(I, H, output_size)

cv2.imshow('I', I)
cv2.waitKey(0)

cv2.imshow('J', J)
cv2.waitKey(0)
