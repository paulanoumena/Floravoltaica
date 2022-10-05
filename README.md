# Floravoltaica
Repository for the codes of the Floravoltaica project.

Each directory is briefly described below and in more detail in the READEME file of each directory.

## The project
The Floravoltaica project consists on installing a Noir camera and calculate the NDVI of the plants with the images obtained.


## NDVI
This section presents the images of the process to calculate the NDVI and obtain a color map image of it.

To calculate the NDVI the first step is to take an image with a camera without and infrared filter.

<img src="https://github.com/paulanoumena/Florovoltaica/blob/main/results/Image1/original_image.jpg" width="200">

Secondly, it is advisable to apply a contrats in the image for better detection.

<img src="https://github.com/paulanoumena/Florovoltaica/blob/main/results/Image1/contrasted_image.jpg" width="200">

Once the contrast is applied it is possible to calculate the NDVI.

<img src="https://github.com/paulanoumena/Florovoltaica/blob/main/results/Image1/ndvi.jpg" width="200">

As the NDVI image seems black for the human sight, it is applied a contrast for better visualization.

<img src="https://github.com/paulanoumena/Florovoltaica/blob/main/results/Image1/ndvi_contrasted.jpg" width="200">

Finally, using the image of the NDVI contrasted it is posible to apply the color mapping representing the NDVI values.

<img src="https://github.com/paulanoumena/Florovoltaica/blob/main/results/Image1/color_map.jpg" width="200">

## Brief explanation of the content of this repository
- src: this folder contains all the code necessary for the correct execution of the NDVI algorithm
- images: this folder contains images taken by a Noir pi camera
- results: this folder contains images showing the steps of the NDVI calculation
