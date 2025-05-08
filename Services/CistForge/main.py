import cv2 as cv
import numpy as np

imgHeigh, imgWidth = 400, 400
thicknes, color, topPoint = 3, (0, 0, 0), 60 # Espessura 6, Cor Black

# Pontos de Referencia para geracao do pino central da imagem
startPoint, endPoint = (imgWidth // 2, topPoint), (imgWidth // 2, imgHeigh - 2*topPoint)

firstImage = np.ones((imgHeigh, imgWidth, 3), dtype=np.uint8) * 255

cv.line(firstImage, startPoint, endPoint, color, thicknes)

cv.imshow("Hello World", firstImage)
k = cv.waitKey(0)