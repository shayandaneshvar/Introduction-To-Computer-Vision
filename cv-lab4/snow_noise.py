import cv2
import numpy as np

I = cv2.imread('isfahan.jpg', cv2.IMREAD_COLOR)
I = I.astype(np.float) / 255

sigma = 0.04  # initial standard deviation of noise
const = 0.01
while True:
    print(f"STD (Sigma)= {sigma}")
    N = np.random.randn(*I.shape) * sigma
    J = I + N  # change this line so J is the noisy image

    cv2.imshow('snow noise', J)

    # press any key to exit
    key = cv2.waitKey(33)
    if key & 0xFF == ord('u'):  # if 'u' is pressed
        # increase noise
        sigma += 0.01
    elif key & 0xFF == ord('d') and sigma - const >= 0:  # if 'd' is pressed
        # decrease noise
        sigma -= const
    elif key & 0xFF == ord('q'):  # if 'q' is pressed then 
        break  # quit
    elif key == ord('r'):
        sigma = 0.04  # reset
cv2.destroyAllWindows()
