import os
import cv2
import numpy as np


def new_size(dims, scale=1):
    width = dims[0]
    height = dims[1]
    k = 49 * scale
    return width + k, height + k


def fry_image(image_directory, filename, scale=6):
    im = cv2.imread(image_directory + filename)

    sharpen = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])

    blur = np.array([[1,2,1],
                     [2,4,2],
                     [1,2,1]]) /16

    # repeated sharpen and blur, simulates lossy compression (gaussian)
    for i in range(scale - 1):
        im = cv2.filter2D(src=im, ddepth=-1, kernel=blur)
        im = cv2.filter2D(src=im, ddepth=-1, kernel=sharpen)

    # repeated resize, simulates blurring
    for i in range(scale + 5):
        im = cv2.resize(im, new_size(im.shape))
        im = cv2.resize(im, new_size(im.shape, scale=-1))

    status = cv2.imwrite("fried/" + filename, im)
    print(status)


if __name__ == '__main__':
    directory = "to_fry/"
    files = os.listdir(directory)

    for image in files:
        fry_image(directory, image, scale=15)