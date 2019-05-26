
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
    "Black": ([0, 0, 0], [0, 0, 50]),
    "Grey": ([0, 0, 51], [0, 0, 235]),
    "White" : ([0, 0, 236], [0, 0, 255]),
    "Bright Red" : ([0, 255, 255], [7, 255, 255]),
    "Orange" : ([8, 255, 255], [15, 255, 255]),
    "Gold" : ([16, 255, 255], [22, 255, 255]),
    "Yellow" : ([23, 255, 255], [34, 255, 255]),
    "Neon Yellow" : ([35, 255, 255] , [42, 255, 255]),
    "Light Green" : ([43, 255, 255], [56, 255, 255]),
    "Green" : ([57, 255, 255], [71, 255, 255]),
    "Seafoam": ([72, 255, 255], [81, 255, 255]),
    "Turquoise" : ([82, 255, 255], [88, 255, 255]),
    "Light Blue" : ([89, 255, 255], [96, 255, 255]),
    "Blue" : ([97, 255, 255], [110, 255, 255]),
    "Dark Blue": ([111, 255, 255], [135, 255, 255]),
    "Purple" : ([136, 255, 255], [145, 255, 255]),
    "Magenta" : ([146, 255, 255], [157, 255, 255]),
    "Hot Pink" : ([158, 255, 255], [162, 255, 255]),
    "Pink" : ([163, 255, 255], [169, 255, 255]),
    "Rasberry" : ([170, 255, 255], [172, 255, 255]),
    "Red" : ([173, 255, 255], [187, 255, 255]),  
    "Brown" : ([0, 90, 90], [0, 170, 170 ]),
    "Dark Green" : ([60, 125, 125], [71, 125, 125]),
    "Dark Red" : ([0, 200, 200], [7, 200, 200])
}

#call function to detect color in the image
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
