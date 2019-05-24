import numpy as np
import matplotlib.pyplot as plt
import cv2


#Helps convert RGB value to HSV value
def HSV(RGB):
    RGB = np.uint8([[RGB]])
    HSV = cv2.cvtColor(RGB, cv2.COLOR_RGB2HSV)
    return HSV


#Dictionary for color ranges
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
    'Dark Blue': ([107,40,40], [115,255,255]),
    'White': ([0,0,0],[0,10,255]),
    'Black': ([0,0,0],[200,255,42])
}


def colorDetection(image):
    #Converts image from BGR to RGB
    BGRimage = cv2.imread(image)
    RGBimage = cv2.cvtColor(BGRimage, cv2.COLOR_BGR2HSV)

    #dictionary to count number of undetected pixels in image for each color
    pixelDict = {}

    #Detection for each colour in image
    for color in colorRanges:
        lowerLimit = np.array(colorRanges[color][0])
        upperLimit = np.array(colorRanges[color][1])
        imageSize = np.shape(RGBimage)
        background = np.zeros((imageSize[1], imageSize[2]))
        mask = cv2.inRange(RGBimage, lowerLimit, upperLimit)
        detection = cv2.bitwise_and(RGBimage, RGBimage, mask=mask)
        pixelCount = 0
        for pixel in detection:
            if pixel.any() == background.any():
                pixelCount += 1
                pixelDict[color] = pixelCount
                
    #List of most dominant colors in the image
    color = []
    minKey = min(pixelDict, key = pixelDict.get)
    for key in pixelDict:
        if pixelDict[key] == pixelDict[minKey]:
            color.append(key)
    return color