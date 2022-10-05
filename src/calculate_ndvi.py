import cv2
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
from fastiecm import fastiecm
from imageio import imread, imwrite
from PIL import Image
import json
from utils import display, contrast_stretch, calc_ndvi, resize
from Segmentation import segmentation


# CALCULATE NDVI _______________________________________________________________________________________________________________________________________

# Defaults
save_images = False
save_json = False
display_ = False

# Read images
img = cv2.imread('/home/noumena/Documents/2022_03_FLORAVOLTAICA/Original_images/image2.jpg')

# Resize images
img = resize(img)

# Apply contrast
contrasted = contrast_stretch(img)

# Calculate ndvi
ndvi = calc_ndvi(contrasted)
avg_ndvi = np.mean(ndvi) # In case we want to map the values to a new scale --> ndvi = np.interp(ndvi, (ndvi.min(), ndvi.max()), (0, 0.5))
print('NDVI without segmentation: ', avg_ndvi)

# Apply contrast to NDVI
ndvi_contrasted = contrast_stretch(ndvi)

# Color mapping
color_mapped_prep = ndvi_contrasted.astype(np.uint8)
color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)

# Save .json
if save_json:
    data = {
        "NDVI:":{
            "NDVI without segementation": float(avg_ndvi),
        },
    }

    path_ = '/home/noumena/Documents/2022_03_FLORAVOLTAICA/Image_results/Image2/'

    with open(path_ + 'json_data.json', 'w') as outfile:
        json.dump(data, outfile)
        outfile.close()

# Save images
if save_images:
    path_ = '/home/noumena/Documents/2022_03_FLORAVOLTAICA/Image_results/Image2/'
    cv2.imwrite(path_ + 'original_image.jpg', img)
    cv2.imwrite(path_ + 'contrasted_image.jpg', contrasted)
    cv2.imwrite(path_ + 'ndvi.jpg', ndvi)
    cv2.imwrite(path_ + 'ndvi_contrasted.jpg', ndvi_contrasted)
    cv2.imwrite(path_ + 'color_map.jpg', color_mapped_image)

# Display images
if display:
    display(img, 'Original Image')
    display(img, 'Image contrasted')
    display(ndvi, 'NDVI')
    display(ndvi_contrasted, 'NDVI Contrasted') 
    display(color_mapped_image, 'NDVI color mapped')