
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import cv2


# In[341]:


RGB = np.uint8([[[0,8,8]]])
HSV = cv2.cvtColor(RGB, cv2.COLOR_RGB2HSV)
print(HSV)


# In[454]:


colorRanges = {
    'Light blue': ([95,40,40],[102,255,255]),
    'Orange': ([14,40,40], [24,255,255]),
    'Dark Orange': ([6,40,40], [10,100,100]),
    'Dark Red': ([[0, 40, 40]], [0, 255, 255]),
    'Red': ([170, 40, 40], [180, 255, 255]),
    'Gold': ([[21,40,40]], [26,255,255]),
    'Yellow': ([27,40,40],[35,255,255]),
    'Light Green': ([32,40,40], [40,255,255]),
    'Green' : ([40,40,40], [50,255,255]),
    'Teal': ([84,40,40], [88,255,255]),
    'Dark Green': ([64,40,40],[72,255,255]),
    'Blue': ([102,40,40], [106,40,40]),
    'Dark Blue': ([107,40,40], [115,255,255]),
    'White': ([0,0,0],[0,10,255]),
    'Black': ([0,0,0],[200,255,42])
}


# In[455]:


BGRimage = cv2.imread('remote.jpg')
RGBimage = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2HSV)

blueCounter = 0
greenCounter = 0
orangeCounter = 0
blueDetect = 0
greenDetect = 0
orangeDetect = 0
#checking for colours
for color in colorRanges:
    lowerLimit = np.array(colorRanges[color][0])
    upperLimit = np.array(colorRanges[color][1])
    imageSize = np.shape(RGBimage)
    verifyPixel = np.zeros((imageSize[1], imageSize[2]))
    mask = cv2.inRange(RGBimage, lowerLimit, upperLimit)
    detection = cv2.bitwise_and(RGBimage, RGBimage, mask=mask)
    for pixel in detection:
        if pixel.any() == verifyPixel.any():
            if color == 'Blue':
                blueCounter += 1
                blueDetect = detection
            elif color =='Green':
                greenCounter += 1
                greenDetect = detection
            else:
                orangeCounter += 1
                orangeDetect = detection
if blueCounter>greenCounter and orangeCounter>greenCounter:
    print("The object is green.")
elif greenCounter>blueCounter and orangeCounter>blueCounter:
    print("The object is blue")
elif blueCounter>orangeCounter and greenCounter>orangeCounter:
    print("The object is orange")
else:
    print("The object is neither blue, green or orange")


# In[456]:


BGRimage = cv2.imread('car.jpg')
RGBimage = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2HSV)
lowerLimit = np.array([0,0,0])
upperLimit = np.array([200,255,42])
imageSize = np.shape(RGBimage)
verifyPixel = np.zeros((imageSize[1], imageSize[2]))
mask = cv2.inRange(RGBimage, lowerLimit, upperLimit)
detection = cv2.bitwise_and(RGBimage, RGBimage, mask=mask)
plt.imshow(detection)

