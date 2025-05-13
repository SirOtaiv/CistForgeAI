import cv2 as cv
import numpy as np

from Services.CistForge.quadrants.unit import unitLineGenerator

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

firstImage = np.ones((x, x, 3), dtype=np.uint8) * 255

# Criando a linha central
cv.line(firstImage, pointBlocks[1], pointBlocks[10], color, thicknes)

# Gerando usando função
firstImage = unitLineGenerator(2, firstImage, pointBlocks, {"color": color, "thickness": thicknes})

cv.imshow("Hello World", firstImage)
k = cv.waitKey(0)