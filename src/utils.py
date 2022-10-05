#
# This file contains all the useful functions to calculate NDVI_____________________________________________________________________________________
#

import cv2
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
from PIL import Image


def display(image, image_name):
    image = np.array(image, dtype=float)/float(255)
    shape = image.shape
    height = int(shape[0] / 2)
    width = int(shape[1] / 2)
    image = cv2.resize(image, (width, height))
    cv2.namedWindow(image_name)
    cv2.imshow(image_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def contrast_stretch(im):
    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)

    out_min = 0.0
    out_max = 255.0

    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min

    return out


def calc_ndvi(image):
    b, g, r = cv2.split(image)
    bottom = (r.astype(float) + b.astype(float))
    bottom[bottom==0] = 0.01
    #ndvi = (b.astype(float) - r) / bottom  # FOR OTHER CAMERAS (RED CHANNEL)
    ndvi = (r.astype(float) - b) / bottom   # FOR NOIR RPI CAMERA (BLUE CHANNEL)

    return ndvi


# We resize img because increase speed when apply mask
def resize(img):

    scale_percent = 15 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    return img


def color_seg(img):

    #....... COLOR SEGMENTATION .......

    blur = cv2.blur(img,(5,5))
    blur0=cv2.medianBlur(blur,5)
    blur1= cv2.GaussianBlur(blur0,(5,5),0)
    blur2= cv2.bilateralFilter(blur1,9,75,75)

    hsv = cv2.cvtColor(blur2, cv2.COLOR_BGR2HSV)

    # color filter
    low_green = np.array([10, 10, 10])
    high_green = np.array([150, 150, 150])
    mask = cv2.inRange(hsv, low_green, high_green)

    res = cv2.bitwise_and(img,img, mask= mask)

    return res


def apply_mask(image, mask):

    #Tranform green to 1
    for row in range(mask.shape[0]):
        for column in range(mask.shape[1]):
            if mask[row][column] > 250:
                mask[row][column] = 1 #posem el numero 1 perque aixi al multiplicar quedar igual
            else:
                mask[row][column]= 0
        #create segmented image
    segmented_image1 = image*mask

    return segmented_image1