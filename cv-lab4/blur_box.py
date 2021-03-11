import cv2
import numpy as np

I = cv2.imread('isfahan.jpg').astype(np.float64) / 255

# display the original image
cv2.imshow('original', I)
cv2.waitKey()

# creating a box filter
m = 5  # choose filter size

# create an m by m box filter
F = np.ones((m, m), np.float64) / (m * m)
print(F)

# Now, filter the image
# J = cv2.filter2D(I, -1, F)  # What is ddepth?!
J = cv2.blur(I, (m, m))  # rewrite
cv2.imshow('blurred', J)
cv2.waitKey()

cv2.destroyAllWindows()
