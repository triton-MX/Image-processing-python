# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 16:14:38 2024

@author: Triton Perea

Aplication of Contrast Sctreching algorithm

Reference: Image processing and acquisition using python (2nd ed) by Ravishankar Chityala & 
Sridevi Pudipeddi
    pg: 112

"""
# Import libraries
import cv2

# Path of image file
pathImg = "1000061F.png"

# Opening the image
imge= cv2.imread(pathImg)

# Finding the maximum and minumum pixel values
b = imge.max()
a = imge.min()
#print(a,b)

# Converting imge to float
c = imge.astype(float)

# Constrast streching transformation
imgeCn = 255.0*(c-a)/(b-a+0.0000001)

# Saving the image after the constast transformation
cv2.imwrite("1000061F-PostContrast.png", imgeCn)
