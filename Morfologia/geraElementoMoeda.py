#-*- coding=utf-8 -*-
import numpy as np
import cv2

def geraElemento(img, limite):

    temp = np.copy(img)

    x_min = 0
    x_max = 0
    y_max = 0
    y_min = 0

    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            if(img[y,x] > limite):
                temp[y,x] = 255
                if(x < x_min):
                    x_min = x
                if(x > x_max):
                    x_max = x
                if(y < y_min):
                    y_min = y
                if(y > y_max):
                    y_max = y

    out = np.copy(temp[y_min:y_max, x_min:x_max])
    return out



if __name__ == "__main__":
