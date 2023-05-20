import cv2
import numpy as np
import how_to_acces_and_edit_pixel_value
import time
import mouse_movments_sample

cv2.namedWindow("preview")
vc = cv2.VideoCapture(1)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    img = frame
    rval, frame = vc.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_range = np.array([150, 90, 220]) # najnižja Rdeča barva ki jo zazna 
    upper_range = np.array([255, 255, 255]) # najvišja Rdeča barva ki jo lahko zazna

    mask = cv2.inRange(hsv, lower_range, upper_range)
    cv2.imshow('Rdeč laser', mask)

    '''lower_range = np.array([35, 20, 35]) # najnižja barva ki jo zazna
    upper_range = np.array([150, 255, 150]) # najvišja barva ki jo lahko zazna

    mask = cv2.inRange(hsv, lower_range, upper_range)
    cv2.imshow('Zelen laser', mask)'''

    x, y = how_to_acces_and_edit_pixel_value.white_pixels_detection(mask)
    x = int(x)
    y = int(y)
    print("x",x)  
    print("y", y) 
    ''' if x != 1000 and y != 1500:
        mouse_movments_sample.move(x, y)
        x = 1000
        y = 1500
    '''
        
        
    


    key = cv2.waitKey(20)


    if key == 27: # exit on ESC
        break

cv2.destroyWindow("preview")
vc.release()