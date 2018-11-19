import numpy as np
import cv2 as cv


#Utilizando vizinhanca-4
def segmenta(img):
        num = 0
        label = np.zeros((img.shape[0], img.shape[1]), np.uint8)
        formSize = []

        for x in range(0, img.shape[1]):
            for y in range(0, img.shape[0]):
                if(img[y,x] == 255 and label[y,x] == 0):
                    num += 1
                    formSize.append(1)

                    pilha = [(y,x)]

                    while(pilha):
                        j, i = pilha.pop()

                        label[j,i] = num
                        formSize[num-1] += 1

                        #Verifica se os pixels adjacentes estao dentro da imagem
                        #e se sao Brancos e sem label (para evitar ficar em loop
                        #entre os mesmos pixels)
                        if(j-1 >= 0 and img[j-1, i] == 255 and label[j-1, i] == 0):
                            pilha.append((j-1, i))
                        if(j+1 < img.shape[0] and img[j+1, i] == 255 and label[j+1, i] == 0):
                            pilha.append((j+1, i))
                        if(i-1 >= 0 and img[j, i-1] == 255 and label[j, i-1] == 0):
                            pilha.append((j, i-1))
                        if(i+1 < img.shape[1] and img[j, i+1] == 255 and label[j, i+1] == 0):
                            pilha.append((j, i+1))

        return num