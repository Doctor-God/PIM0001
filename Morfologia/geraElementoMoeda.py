#-*- coding=utf-8 -*-
import numpy as np
import cv2
import sys
import morfo as mo
import matplotlib.pyplot as plt

def geraElemento(img, limite):

    plt.hist(img.ravel(),256,[0,256]); plt.show()

    temp = np.copy(img)


    # cv2.imshow("oi", temp)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    x_min = 0
    x_max = 0
    y_max = 0
    y_min = 0

    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            if(img[y,x] < limite):
                temp[y,x] = 255
                if(x < x_min):
                    x_min = x
                if(x > x_max):
                    x_max = x
                if(y < y_min):
                    y_min = y
                if(y > y_max):
                    y_max = y
            else:
                temp[y,x] = 0
    elem = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))
    elem2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (50,50))

    temp = cv2.dilate(temp, elem, iterations=1)
    temp = cv2.erode(temp, elem, iterations=1)
    temp = cv2.dilate(temp, elem, iterations=1)
    out = cv2.erode(temp, elem, iterations=1)
    out = cv2.erode(out, elem2, iterations = 1)
    # out = temp
    #
    # y_par = False
    # x_par = False
    # if(out.shape[0] % 2 == 0):
    #     y_par = True
    # if(out.shape[1] % 2 == 0):
    #     x_par = True
    #
    #
    # if(y_par and x_par):
    #     new_out = np.zeros((out.shape[0]+1, out.shape[1]+1), np.uint8)
    # elif(y_par):
    #     new_out = np.zeros((out.shape[0]+1, out.shape[1]), np.uint8)
    # elif(x_par):
    #     new_out = np.zeros((out.shape[0], out.shape[1]+1), np.uint8)
    # else:
    #     new_out = np.zeros((out.shape[0], out.shape[1]), np.uint8)
    #
    #
    # new_out[0:out.shape[0], 0:out.shape[1]] = out
    #
    # cv2.imshow("oi", out)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    #
    # out = np.copy(temp[y_min:y_max, x_min:x_max])
    # out = np.where(out < limite, 0, 255)
    # return new_out
    return out


if __name__ == "__main__":
    #argv[1] = imagem para a qual queremos elemento
    #argv[2] = imagem dilatador do elemento (para gerar elemento levemente maior)
    #argv[3] = threshold para limiarização
    argv = sys.argv
    img = cv2.imread(argv[1], 0)
    name_ext = argv[1].split('.')
    elem = geraElemento(img, int(argv[2]))
    cv2.imwrite(name_ext[0] + "_elem." + name_ext[1], elem)
