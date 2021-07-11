import cv2
import numpy as np

I = cv2.imread('sign.jpg')

p1 = (135, 105)
p2 = (331, 143)
p3 = (356, 292)
p4 = (136, 290)

points1 = np.array([p1, p2, p3, p4], dtype=np.float32)

n = 480
m = 320
output_size = (n, m)
points2 = np.array([(0, 0),
                    (n, 0),
                    (n, m),
                    (0, m)]).astype(np.float32)

H = cv2.getPerspectiveTransform(points1, points2)
J = cv2.warpPerspective(I, H, output_size)

# mark corners of the plate in image I
for i in range(4):
    cv2.circle(I, (points1[i, 0], points1[i, 1]), 5, [0, 0, 255], 2)
    cv2.circle(J, (points2[i, 0], points2[i, 1]), 3, [0, 0, 255], 2)

cv2.imshow('I', I)
cv2.waitKey(0)

cv2.imshow('J', J)
cv2.waitKey(0)
