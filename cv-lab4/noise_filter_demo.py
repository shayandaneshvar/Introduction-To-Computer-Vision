import cv2
import numpy as np

I = cv2.imread('branches2.jpg').astype(np.float32) / 255

noise_sigma = 0.04  # initial standard deviation of noise

m = 1  # initial filter size,

gm = 3  # gaussian filter size

size = 9  # bilateral filter size
sigmaColor = 0.3
sigmaSpace = 75

# with m = 1 the input image will not change
filter = 'b'  # box filter
const = 0.01
while True:

    # add noise to image
    N = np.random.rand(*I.shape) * noise_sigma
    J = (I + N).astype(np.float32)
    K = J
    if filter == 'b':
        K = cv2.blur(J, (m, m))
    elif filter == 'g':
        K = cv2.GaussianBlur(J, (gm, gm), 0)
    elif filter == 'l':
        K = cv2.bilateralFilter(J, size, sigmaColor, sigmaSpace)

    # filtered image
    cv2.imshow('img', K)
    key = cv2.waitKey(30) & 0xFF

    if key == ord('b'):
        filter = 'b'  # box filter
        print('Box filter')

    elif key == ord('g'):
        filter = 'g'  # filter with a Gaussian filter
        print('Gaussian filter')

    elif key == ord('l'):
        filter = 'l'  # filter with a bilateral filter
        print('Bilateral filter')

    elif key == ord('+'):
        # increase m
        m = m + 2
        print('m=', m)

    elif key == ord('-'):
        # decrease m
        if m >= 3:
            m = m - 2
        print('m=', m)
    elif key == ord('u'):
        noise_sigma += 0.01
        print(f"noise sigma {noise_sigma}")
    elif key == ord('d') and noise_sigma - const >= 0:
        noise_sigma -= const
        print(f"noise sigma {noise_sigma}")
    elif key == ord('p'):
        # increase gm
        if filter == 'g':
            gm += 2
            print(f"gm = {gm}")
        elif filter == 'l':
            sigmaColor += 0.1 # best value is about 0.5
            print(f"sigma_color = {sigmaColor}")
    elif key == ord('n'):
        # decrease gm
        if filter == 'g':
            gm = max(gm - 2, 1)
            print(f"gm = {gm}")
        elif filter == 'l':
            sigmaColor = max(sigmaColor - 0.1, 0.1)
            print(f"sigma_color = {sigmaColor}")
    elif key == ord('>'):
        size += 2
        print(f"size = {size}")
    elif key == ord('<'):
        # decrease size
        size = max(size - 2, 1)
        print(f"size = {size}")
    elif key == ord('q'):
        break  # quit
    # Extra -> best value is about 80
    elif key == ord("s"):
        sigmaSpace += 1
        print(f"sigmaSpace = {sigmaSpace}")
    elif key == ord("a"):
        sigmaSpace = max(sigmaSpace - 1, 1)
        print(f"sigmaSpace = {sigmaSpace}")
cv2.destroyAllWindows()
