
# coding: utf-8

# In[47]:


import numpy as np
import matplotlib.pyplot as plt
import cv2
import time 


## converts RBG to HSV
RGB = np.uint8([[[177, 255, 255]]])
HSV = cv2.cvtColor(RGB, cv2.COLOR_RGB2HSV)
print(HSV)


# In[31]:


colorRanges = {
    'Blue': ([100,150,0],[140,255,250]),
    'Green': ([40,100,150],[80,255,255]),
    'Orange': ([1,100,150], [18,255,255]),
    'Black': ([0, 0, 0], [180, 255, 30]),
    'Red': ([0, 163, 255], [0, 255, 255]),
    'Salmon': ([0, 32, 255], [0, 96, 255]),
    'Pink': ([155, 78, 255], [155, 255, 255]),
    'Teal': ([87, 78, 255], [87, 255, 255]),
    
}


# In[32]:


def get_color(image: str):
    tic = time.time()
    BGRImage = cv2.imread(image)
    RGBimage = cv2.cvtColor(BGRImage, cv2.COLOR_BGR2HSV)
    colors_list = []
    color_detection = []
    new_dict = dict()
    for color in colorRanges:
        counter = 0
        lowerLimit = np.array(colorRanges[color][0])
        upperLimit = np.array(colorRanges[color][1])
        imageSize = np.shape(RGBimage)
        verifyPixel = np.zeros((imageSize[1], imageSize[2]))
        mask = cv2.inRange(RGBimage, lowerLimit, upperLimit)
        detection = cv2.bitwise_and(RGBimage, RGBimage, mask=mask)
        plt.imshow(detection)
        for pixel in detection:
            if pixel.any() == verifyPixel.any():
                counter +=1 
        colors_list.append(color)
        color_detection.append(counter)
        new_dict[color] = counter
    minimum = min(color_detection)
    min_index = color_detection.index(minimum) 
    min_colors = []
    for key in new_dict:
        if new_dict[key] == minimum:
            min_colors.append(key)
    tock = time.time()
    if len(min_colors) > 1:
        output = 'this image is a mix of ; '
        for color in min_colors:
            output += color + " "
        return output
    return ("the color of this image is " + colors_list[min_index])
    #return tock - tic

        


# In[33]:


get_color('xbox.jpeg')

