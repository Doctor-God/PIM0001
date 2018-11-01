#-*- coding=utf-8 -*-

import numpy as np
import cv2

def dilata(img, elem):
    # elem = np.zeros((30,30), np.uint8)
    out = np.zeros(img.shape, np.uint8)

    # out[::] = 255
    elem_center = (elem.size[0]/2, elem.size[1]/2) #Centro do elemento (no caso da esfera pixel [9,9])


    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            if(img[y,x] == 255):
                for xe in range(elem.shape[1]):
                    for ye in range(elem.shape[0]):
                        if(elem[ye,xe] == 255):
                            out[y+ye, x+xe] = 255
    return out

def erode(img, elem):
    # elem = np.zeros((30,30), np.uint8)
    out = np.zeros(img.shape, np.uint8)

    # out[::] = 255

    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            if(img[y,x] == 255):
                for xe in range(elem.shape[1]):
                    fail = False
                    for ye in range(elem.shape[0]):
                        if(elem[ye,xe] == 255):
                            if(img[y+ye, x+xe] == 0):
                                fail = True
                                break
                    if(fail):
                        break
                else:
                    out[y,x] = 255
    return out

# if __name__ == "__main__":
#     img = cv2.imread("hourglass.png", 0)
#
#     nova = erode(img)
#     nova = dilata(nova)
#
#     cv2.imwrite("hourglass_dilatada.png", nova)
#     cv2.imshow("OLoko", nova)
#     cv2.waitKey()
#     cv2.destroyAllWindows()
