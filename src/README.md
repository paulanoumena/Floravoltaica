# Floravoltaica codes
Final code of the Floravoltaica project implemented by Noumena.

## Requeriments
- [OpenCV](https://www.pyimagesearch.com/2020/02/03/how-to-use-opencvs-dnn-module-with-nvidia-gpus-cuda-and-cudnn/)
- Numpy
- Imageio
- Pillow
- Json

Create a workon virtual environment. 
Configure python3 as the default python interpreter for this venv.

## Workflow
#### calculate_ndvi.py
This is the main code were you can find all the steps to perfom the NDVI calculation. 
- Input: image taken by a without an infrared filter.
- Output: NDVI value

This file lets you save the images showing the steps of the NDVI calculation as well as a JSON file with the NDVI value.

#### utils.py
This file contains all the functions necessary to perfom the NDVI calculation. 

#### segmentation.py
This file contains a function to perform the segmentation of the plants. In this segmentation it is employed the resulting NDVI contrasted image which is binarized and used as a mask. Once the segmentation is performed it recalculates the NDVI.

#### fastiecm.py
This file contains a function to perfrom color mapping to represent the NDVI values on the image.
