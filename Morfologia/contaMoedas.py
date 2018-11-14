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
    return out

def conta(img, limite):
    elem_1r = cv2.imread("Imagens/moeda_1r_elem.jpg", 0)
    elem_50 = cv2.imread("Imagens/moeda_50_elem.jpg", 0)
    elem_25 = cv2.imread("Imagens/moeda_25_elem.jpg", 0)
    elem_10 = cv2.imread("Imagens/moeda_10_elem.jpg", 0)
    elem_5 = cv2.imread("Imagens/moeda_5_elem.jpg", 0)

    img = thresholding(img, limite)
    cv2.imshow("oi", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

    # elem = cv2.imread("Imagens/elemento_esfera_maior.png", 0)
    # temp = mo.dilata(img, elem)

    temp = mo.erode(img, elem_10)
    cv2.imshow("oi", temp)
    cv2.waitKey()
    cv2.destroyAllWindows()


def main(argv):
    #argv[1] = imagem a contar moedas
    #argv[2] = limiar
    if(len(argv) != 3):
        print("python contaMoedas.py img limiar")
        exit()

    img = cv2.imread(argv[1], 0)
    valor = conta(img, int(argv[2]))

if __name__ == "__main__":
    main(sys.argv)
