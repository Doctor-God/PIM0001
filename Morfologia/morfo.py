#-*- coding=utf-8 -*-

import numpy as np
import cv2

def dilata(img):
    elem = np.zeros((30,30), np.uint8)
    out = np.zeros(img.shape, np.uint8)

    out[::] = 255

    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            if(img[y,x] == 0):
                for xe in range(elem.shape[1]):
                    for ye in range(elem.shape[0]):
                        out[y+ye, x+xe] = 0
    return out

def erode(img):
    elem = np.zeros((30,30), np.uint8)
    out = np.zeros(img.shape, np.uint8)

    out[::] = 255

    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            if(img[y,x] == 0):
                for xe in range(elem.shape[1]):
                    fail = False
                    for ye in range(elem.shape[0]):
                        if(img[y+ye, x+xe] == 255):
                            fail = True
                            break
                    if(fail):
                        break
                else:
                    out[y,x] = 0
    return out

if __name__ == "__main__":
    img = cv2.imread("hourglass.png", 0)

    nova = erode(img)
    nova = dilata(nova)

    cv2.imwrite("hourglass_dilatada.png", nova)
    cv2.imshow("OLoko", nova)
    cv2.waitKey()
    cv2.destroyAllWindows()
