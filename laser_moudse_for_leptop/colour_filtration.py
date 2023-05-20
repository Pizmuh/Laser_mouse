import numpy as np
import cv2
import how_to_acces_and_edit_pixel_value
import mouse_movments_sample
import time
from PIL import Image



cap = cv2.VideoCapture(1)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    img = frame

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # MODRA lower_range = np.array([90, 90, 200]) # najnižja barva ki jo zazna
    # MODRA upper_range = np.array([255, 255, 255]) # najvišja barva ki jo lahko zazna
    # zelena lower_range = np.array([30, 30, 30]) # najnižja barva ki jo zazna
    # zelena upper_range = np.array([255, 255, 255]) # najvišja barva ki jo lahko zazna

    lower_range = np.array([150, 90, 220]) # najnižja barva ki jo zazna
    upper_range = np.array([255, 255, 255]) # najvišja barva ki jo lahko zazna

    mask = cv2.inRange(hsv, lower_range, upper_range)
    cv2.imshow('frame', mask)

    # avragein off white spaces
    x, y = how_to_acces_and_edit_pixel_value.white_pixels_detection(mask)


    x = int(x)
    y = int(y)
    print("x",x)  
    print("y", y) 
    if x != 1000 & y != 1500:
        mouse_movments_sample.move(x, y)
        time.sleep(10)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
