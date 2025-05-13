import cv2 as cv
import numpy as np

x = 400
thicknes, color, zPoint = 3, (0, 0, 0), 60

aPoint, bPoint = (x // 2), (x - zPoint)
tPoint = bPoint // 4

pointBlocks = [
    (aPoint - tPoint, zPoint),             # 1
    (aPoint, zPoint),                      # 2
    (aPoint + tPoint, zPoint),             # 3

    (aPoint - tPoint, zPoint + tPoint),    # 4
    (aPoint, zPoint + tPoint),             # 5
    (aPoint + tPoint, zPoint + tPoint),    # 6

    (aPoint - tPoint, bPoint - tPoint),    # 7
    (aPoint, bPoint - tPoint),             # 8
    (aPoint + tPoint, bPoint - tPoint),    # 9

    (aPoint - tPoint, bPoint),             # 10
    (aPoint, bPoint),                      # 11
    (aPoint + tPoint, bPoint),             # 12
    ]

# Pontos de Referencia para geracao do pino central da imagem
startPoint, endPoint = pointBlocks[1], pointBlocks[10]

firstImage = np.ones((x, x, 3), dtype=np.uint8) * 255

# Criando a linha central
cv.line(firstImage, pointBlocks[1], pointBlocks[10], color, thicknes)

# Printando numero 1
cv.line(firstImage, pointBlocks[1], pointBlocks[2], color, thicknes)

# Printando numero 20
cv.line(firstImage, pointBlocks[3], pointBlocks[4], color, thicknes)

# Printando numero 400
cv.line(firstImage, pointBlocks[7], pointBlocks[11], color, thicknes)

# Printando numero 6000
cv.line(firstImage, pointBlocks[6], pointBlocks[9], color, thicknes)

cv.imshow("Hello World", firstImage)
k = cv.waitKey(0)