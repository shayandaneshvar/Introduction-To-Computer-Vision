import cv2
import numpy as np
from matplotlib import pyplot as plt


def get_min_max(image, i):
    if image[i] > image[i + 1]:
        return image[i + 1], image[i]
    else:
        return image[i], image[i + 1]


def count_more(arr, value):
    return len(list(filter(lambda x: x >= value, arr)))


def count_less(arr, value):
    return len(list(filter(lambda x: x <= value, arr)))


def find_min_max(image, lower_bound=-1, higher_bound=256):
    maximum = 0
    minimum = 255
    for i in range(0, len(image) - 1, 2):
        (c_min, c_max) = get_min_max(image, i)
        if maximum < c_max < higher_bound:
            maximum = c_max
        if minimum > c_min > lower_bound:
            minimum = c_min
    return minimum, maximum


def get_ab(image):
    threshold = len(image) * .01
    low = -1
    high = 256
    while True:
        (minimum, maximum) = find_min_max(image, low, high)
        flag = False
        if count_less(image, minimum) < threshold:
            low = minimum
            flag = True
        if count_more(image, maximum) < threshold:
            high = maximum
            flag = True
        if not flag:
            return minimum, maximum


fname = 'crayfish.jpg'
# fname = 'office.jpg'
# fname = 'train.jpg'
# fname = 'terrain.jpg'
# fname = 'map.jpg'
# fname = 'branches.jpg'

I = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)

f, axes = plt.subplots(2, 3)

axes[0, 0].imshow(I, 'gray', vmin=0, vmax=255)
axes[0, 0].axis('off')
axes[1, 0].hist(I.ravel(), 256, [0, 256])

# find by hand
#a = 100 # for crayfish
#b = 170 # for crayfish

# Extra - finds a & b automatically
(a, b) = get_ab(I.ravel())

print(f"a={a},b={b}")

J = (I - a) * 255.0 / (b - a)
J[J < 0] = 0
J[J > 255] = 255
J = J.astype(np.uint8)
axes[0, 1].imshow(J, 'gray', vmin=0, vmax=255)
axes[0, 1].axis('off')
axes[1, 1].hist(J.ravel(), 256, [0, 256])

K = cv2.equalizeHist(I)
axes[0, 2].imshow(K, 'gray', vmin=0, vmax=255)
axes[0, 2].axis('off')
axes[1, 2].hist(K.ravel(), 256, [0, 256])

plt.show()
