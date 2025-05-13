import cv2 as cv
import numpy as np

from Services.CistForge.quadrants.cent import centLineGenerator
from Services.CistForge.quadrants.hundred import hundredLineGenerator
from Services.CistForge.quadrants.thousand import thousandLineGenerator
from Services.CistForge.quadrants.unit import unitLineGenerator

def split_digits(n: int, length: int = 4) -> list[int]:
    return list(map(int, str(n).zfill(length)))

def generate_cistercience_number(n: int) -> np.ndarray:

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

    cistercience_number = np.ones((x, x, 3), dtype=np.uint8) * 255

    # Criando a linha central
    cv.line(cistercience_number, pointBlocks[1], pointBlocks[10], color, thicknes)

    # Separando o numero
    m, c, d, u = split_digits(n)

    # Gerando unidade 1
    cistercience_number = unitLineGenerator(u, cistercience_number, pointBlocks, {"color": color, "thickness": thicknes})

    # Gerando unidade 10
    cistercience_number = centLineGenerator(d, cistercience_number, pointBlocks, {"color": color, "thickness": thicknes})

    # Gerando unidade 100
    cistercience_number = hundredLineGenerator(c, cistercience_number, pointBlocks, {"color": color, "thickness": thicknes})

    # Gerando unidade 10000
    cistercience_number = thousandLineGenerator(m, cistercience_number, pointBlocks, {"color": color, "thickness": thicknes})

    return cistercience_number, n

if __name__ == "__main__":

    number_c, original = generate_cistercience_number(input("Insira um numero entre 0 e 9999:\n"))
    cv.imshow(f"{original}:", number_c)
    k = cv.waitKey(0)