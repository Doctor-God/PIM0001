import numpy as np
import cv2
import sys
import morfo as mo

def thresholding(img, limite):
    out = np.zeros(img.shape, np.uint8)
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            if(img[y,x] < limite):
                out[y,x] = 255

def conta(img, limite):
    img = thresholding(img, limite)
    



def main(argv):
    #argv[1] = imagem a contar moedas
    #argv[2] = limiar
    img = cv2.imread(argv[1], 0)
    valor = conta(img, int(argv[2]))

if __name__ == "__main__":
    main(sys.argv)
