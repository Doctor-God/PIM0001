#-*- coding=utf-8 -*-
import numpy as np
import cv2
import sys
import morfo as mo
import matplotlib.pyplot as plt

def borderLim(img):
    def borderize(img, a, b, out):
        if(out[a, b] == 0):
            return
        pilha.append((a,b))
        while(pilha != []):
            (y,x) = pilha.pop()
            out[y,x] = 0
            if(y-1 >= 0):
                if((img[y-1,x] >= img[y,x] -1 and img[y-1,x] <= img[y,x] +1) and out[y-1, x] != 0):
                    pilha.append((y-1,x))
            if(y+1 < img.shape[0]):
                if((img[y+1,x] >= img[y,x] -1 and img[y+1,x] <= img[y,x] +1) and out[y+1, x] != 0):
                    pilha.append((y+1,x))
            if(x-1 >= 0):
                if((img[y,x-1] >= img[y,x] -1 and img[y,x-1] <= img[y,x] +1) and out[y, x-1] != 0):
                    pilha.append((y,x-1))
            if(x+1 < img.shape[1]):
                if((img[y,x+1] >= img[y,x] -1 and img[y,x+1] <= img[y,x] +1) and out[y, x+1] != 0):
                    pilha.append((y,x+1))

    out = np.ones(img.shape, np.uint8)
    pilha = []
    borderize(img, 0, 0, out)
    print("oi")
    borderize(img, 0, img.shape[1]-1, out)
    print("oi")
    borderize(img, img.shape[1]-1, 0, out)
    print("oi")
    borderize(img, img.shape[1]-1, img.shape[1]-1, out)

    return out



def geraElemento(img, dilat, limite):

    # plt.hist(img.ravel(),256,[0,256]); plt.show()

    temp = np.copy(img)

    temp = borderLim(temp)

    cv2.imshow("oi", temp)
    cv2.waitKey()
    cv2.destroyAllWindows()

    # x_min = 0
    # x_max = 0
    # y_max = 0
    # y_min = 0

    # for x in range(img.shape[1]):
    #     for y in range(img.shape[0]):
    #         if(img[y,x] < limite):
    #             temp[y,x] = 255
    #             if(x < x_min):
    #                 x_min = x
    #             if(x > x_max):
    #                 x_max = x
    #             if(y < y_min):
    #                 y_min = y
    #             if(y > y_max):
    #                 y_max = y
    #         else:
    #             temp[y,x] = 0
    # out = mo.erode(temp, dilat)
    # out = temp
    
    # y_par = False
    # x_par = False
    # if(out.shape[0] % 2 == 0):
    #     y_par = True
    # if(out.shape[1] % 2 == 0):
    #     x_par = True


    # if(y_par and x_par):
    #     new_out = np.zeros((out.shape[0]+1, out.shape[1]+1), np.uint8)
    # elif(y_par):
    #     new_out = np.zeros((out.shape[0]+1, out.shape[1]), np.uint8)
    # elif(x_par):
    #     new_out = np.zeros((out.shape[0], out.shape[1]+1), np.uint8)
    # else:
    #     new_out = np.zeros((out.shape[0], out.shape[1]), np.uint8)


    # new_out[0:out.shape[0], 0:out.shape[1]] = out

    # cv2.imshow("oi", out)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

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
    dilatador = cv2.imread(argv[2], 0)
    name_ext = argv[1].split('.')
    elem = geraElemento(img, dilatador, int(argv[3]))
    cv2.imwrite(name_ext[0] + "_elem." + name_ext[1], elem)
