# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 13:35:39 2024

@author: Triton Perea

Aplication of Contrast Limited Adaptive Histogram Equalization (CLAHE) algorithm

Reference: Image processing and acquisition using python (2nd ed) by Ravishankar Chityala & 
Sridevi Pudipeddi
    pg: 110
"""
# Import libraries
import cv2
from skimage.exposure import equalize_adapthist


# Path of image file
pathImg = "10000627.png"

# Import image from a absolute path
image = cv2.imread(pathImg)#, cv2.IMREAD_GRAYSCALE)
#cv2.imshow("Image", image)

""" I use a cycle to test various constrast values and observe the changes when 
    processing the image
"""
for i in range(0,10):
    # Applying CLAHE
    limit= i*0.01
    image2 = equalize_adapthist(image, clip_limit= 0.02)
    
    # Rescaling image2 from 0 to 255 (L = 2^8) --> i.e. 8-bit grayscale image
    image3 = image2*255.0
    
    BLACK = (255,255,255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_size = 1.1
    font_color = BLACK
    font_thickness = 2
    text = 'CLAHE: 0.02'
    x,y = 10,650
    img_text = cv2.putText(image3, text, (x,y), font, font_size, font_color, font_thickness, cv2.LINE_AA)
    
    newPath= "10000627-PostCLAHE-"+str(limit)+".png"
    # Saving image 3 in a absolute path
    cv2.imwrite(newPath,image3)
    
    pass
