import cv2 as cv
import numpy as np

# .imread função de leitura de um arquivo de image pela Lib OpenCV
img = cv.imread("../../Temp/images/NoobsCorpScreenHoot.jpg")

# Variaveis para apoio a funções
imgHeigh, imgWidth = 400, 200
thicknes, color = 6, (0, 0, 0) # Espessura 6, Cor Black

# .imshow abre a janela para debug da imagem
cv.imshow("Display window", img)

# waitKey() faz esperar uma tecla para fechar a janela da imagem gerada
k = cv.waitKey(0) # Wait for a keystroke in the window

# .ones gera uma image usando ((Altura X Largura, Canais[Quantidade de Cores]), dtype= Tipo de dado [Pra poder variar de 0 a 255])
firstImage = np.ones((imgHeigh, imgWidth, 3), dtype=np.uint8) * 255