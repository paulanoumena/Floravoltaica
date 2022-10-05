#
# This file contains all the steps to perform the segmentaion using the binarization of the ndvi_contrasted image_____________________________________

import cv2
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
from fastiecm import fastiecm
from PIL import Image
from utils import display, contrast_stretch, calc_ndvi, resize, apply_mask

def segmentation(ndvi, ndvi_contrasted, path_):
    # Gray image to Black and white
    (thresh, blackAndWhiteImage) = cv2.threshold(ndvi_contrasted, 230, 255, cv2.THRESH_BINARY)
    display(blackAndWhiteImage, 'blackAndWhiteImage')
    cv2.imwrite(path_ + 'segmentation_mask.jpg', blackAndWhiteImage)

    # Apply mask
    img_masked = apply_mask(ndvi , blackAndWhiteImage)
    non_zero = img_masked[img_masked != 0]
    display(img_masked, 'img_masked')

    # Apply contrast to save image
    ndvi_seg_contrasted = contrast_stretch(img_masked)
    cv2.imwrite(path_ + 'segmented_image.jpg', ndvi_seg_contrasted)

    # Color mapping of segmented image
    color_mapped_prep = ndvi_seg_contrasted.astype(np.uint8)
    color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)
    display(color_mapped_image, 'Color mapped')
    cv2.imwrite(path_ + 'segmented_colormap.jpg', color_mapped_image)

    # Show NDVI result
    ndvi_segmentation = np.mean(non_zero)
    print('NDVI with segmentation: ', ndvi_segmentation)

    return ndvi_segmentation