import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img.png')

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def white_pixels_detection(img):


    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    colour = (0, 0, 0)
    indices = np.where(img == colour)
    unique_coordinates = list(zip(indices[0], indices[1]))

    x_data = []
    y_data = []

    for x, y in unique_coordinates:
        x_data.append(x)
        y_data.append(y)

    x = (((mean(x_data) - 237) * 2000) - 4000)
    y = (((mean(y_data) - 318) * 2000) - 1500)

    return x, y

"""
x_data, y_data = white_pixels_detection(img)
print(x_data)


plt.plot(y_data, x_data, 'co')
plt.axis()
plt.show()

"""