#-*- coding=utf-8 -*-

import numpy as np
import cv2
import sys
import morfo as mo
import segmenta as seg
import matplotlib.pyplot as plt

def thresholding(img, limite):
    out = np.zeros(img.shape, np.uint8)
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            if(img[y,x] < limite):
                out[y,x] = 255

    elem = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (50,50))

    out = cv2.dilate(out, elem, iterations=1)
    out = cv2.erode(out, elem, iterations=1)
    out = cv2.dilate(out, elem, iterations=1)
    out = cv2.erode(out, elem, iterations=1)

    return out

def conta(img, limite, verbose=False):
    elem_1r = cv2.imread("Imagens_reais/moeda_1r_elem.jpg", 0)
    elem_50 = cv2.imread("Imagens_reais/moeda_50_elem.jpg", 0)
    elem_25 = cv2.imread("Imagens_reais/moeda_25_elem.jpg", 0)
    elem_10 = cv2.imread("Imagens_reais/moeda_10_elem.jpg", 0)
    elem_5 = cv2.imread("Imagens_reais/moeda_5_elem.jpg", 0)
    plt.hist(img.ravel(),256,[0,256]); plt.show()

    img_lim = thresholding(img, limite)

    if(verbose):
        sized = cv2.resize(img_lim, (960, 540))
        cv2.imshow("Imagem limiarizada", sized)
        cv2.waitKey()
        cv2.destroyAllWindows()


    temp = cv2.erode(img_lim, elem_5, iterations=1)
    num_1r = seg.segmenta(temp)
    temp = cv2.dilate(temp, elem_5, iterations=1)
    print num_1r
    if(verbose):
        sized = cv2.resize(temp, (960, 540))
        cv2.imshow("Moedas 1r", sized)
        cv2.waitKey()
        cv2.destroyAllWindows()
    #
    #     temp = cv2.erode(img_lim, elem_50, iterations=1)
    #     num_25 = seg.segmenta(temp) - num_1r
    #     temp = cv2.dilate(temp, elem_50, iterations=1)
    #     print num_25
    #     if(verbose):
    #         cv2.imshow("Moedas 1r e 25", temp)
    #         cv2.waitKey()
    #         cv2.destroyAllWindows()
    #
    #         temp = cv2.erode(img_lim, elem_5, iterations=1)
    #         num_50 = seg.segmenta(temp) - (num_1r+num_25)
    #         temp = cv2.dilate(temp, elem_5, iterations=1)
    #         print num_50
    #
    #         if(verbose):
    #             cv2.imshow("Moedas 1r, 25 e 50", temp)
    #             cv2.waitKey()
    #             cv2.destroyAllWindows()
	# temp = cv2.erode(img_lim, elem_10, iterations=1)
	# num_5 = seg.segmenta(temp) - (num_1r + num_25 + num_50)
	# temp = cv2.dilate(temp, elem_10, iterations=1)
	# print num_5
    # if(verbose):
    #     sized = cv2.resize(temp, (960, 540))
    # 	cv2.imshow("Moedas 1r, 25, 50 e 5", sized)
    # 	cv2.waitKey()
    # 	cv2.destroyAllWindows()

	num_10 = seg.segmenta(img_lim) - (num_1r + num_25 + num_50 + num_5)
	print num_10

	valor_moedas = 1.0*num_1r + 0.50*num_50 + 0.25*num_25 + 0.10*num_10 + 0.05*num_5

	return valor_moedas

def main(argv):
    #argv[1] = imagem a contar moedas
    #argv[2] = limiar
    if(len(argv) < 3 or len(argv) > 4):
        print("python contaMoedas.py img limiar [verbose]")
        exit()
    elif(len(argv) == 4):
    	if(argv[3] != "verbose"):
    		print("python contaMoedas.py img limiar verbose")
    		exit()


    img = cv2.imread(argv[1], 0)
    if(len(argv) == 4):
    	valor = conta(img, int(argv[2]), verbose=True)
    else:
    	valor = conta(img, int(argv[2]))

    print("Valor em moedas = R$%.2f" % valor)

if __name__ == "__main__":
    main(sys.argv)
