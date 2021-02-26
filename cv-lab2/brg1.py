import cv2

# import numpy as np
# from matplotlib import pyplot as plt

I = cv2.imread('masoleh.jpg')

# your code ##

# notice that OpenCV uses BGR instead of RGB!
R = I.copy()
G = I.copy()
B = I.copy()
R[:, :, (0, 1)] = 0
G[:, :, (0, 2)] = 0
B[:, :, (1, 2)] = 0

# B = I[:, :, 0]
# G = I[:, :, 1]
# R = I[:, :, 2]

cv2.imshow('win1', I)

while True:
    k = cv2.waitKey()

    if k == ord('o'):
        cv2.imshow('win1', I)
    elif k == ord('b'):
        cv2.imshow('win1', B)
    elif k == ord('g'):
        cv2.imshow('win1', G)
    elif k == ord('r'):
        cv2.imshow('win1', R)
    elif k == ord('q'):
        cv2.destroyAllWindows()
        break
