#-*- coding=utf-8 -*-

import numpy as np
import cv2
from operator import xor

#Os elementos estruturantes devem ter dimensões ímpares para que a origem esteja em um pixel central

def dilata(img, elem):
    out = np.zeros((img.shape[0] + 2*elem.shape[0], img.shape[1] + 2*elem.shape[1]), np.uint8)

    ec = (elem.shape[0]/2, elem.shape[1]/2) #Centro do elemento (no caso da esfera pixel [2,2])

    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            found = False
            for xe in range(-ec[1], ec[1]+1):
                if(found):
                    break
                for ye in range(-ec[0], ec[0]+1):
                    if(y+ye >=0 and y+ye < img.shape[0] and x+xe >=0 and x+xe < img.shape[1]):
                        if(elem[ec[0]+ye, ec[1]+xe] and img[y+ye, x+xe]):
                            out[y+elem.shape[0],x+elem.shape[1]] = 255
                            found = True
                            break

    return out

def erode(img, elem):
    out = np.zeros(img.shape, np.uint8)


    ec = (elem.shape[0]/2, elem.shape[1]/2) #Centro do elemento (no caso da esfera pixel [2,2])


    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            cant_hold = False
            for xe in range(-ec[1], ec[1]+1):
                if(cant_hold):
                    break
                for ye in range(-ec[0], ec[0]+1):
                    if(y+ye >=0 and y+ye < img.shape[0] and x+xe >=0 and x+xe < img.shape[1]):

                        if(elem[ec[0]+ye, ec[1]+xe] and not img[y+ye, x+xe]):
                            cant_hold = True
                            break
                    else:
                        cant_hold = True
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
