import cv2

I = cv2.imread('damavand.jpg')
J = cv2.imread('eram.jpg')
K = I.copy()
cv2.imshow("Blending", K)

for i in range(1, 101):
    cv2.waitKey(100)
    K = cv2.addWeighted(I, 1 - i * 0.01, J, i * 0.01, 0)
    cv2.imshow("Blending", K)

cv2.waitKey()
