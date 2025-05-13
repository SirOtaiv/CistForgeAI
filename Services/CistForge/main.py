import cv2 as cv
import numpy as np

from Services.CistForge.geometry import geometry_points_generate
from Services.CistForge.quadrants.cent import centLineGenerator
from Services.CistForge.quadrants.hundred import hundredLineGenerator
from Services.CistForge.quadrants.thousand import thousandLineGenerator
from Services.CistForge.quadrants.unit import unitLineGenerator

def split_digits(n: int, length: int = 4) -> list[int]:
    return list(map(int, str(n).zfill(length)))

def generate_cistercience_number(n: int) -> np.ndarray:

    geom = geometry_points_generate()

    cistercience_number = np.ones((geom.size, geom.size, 3), dtype=np.uint8) * 255

    # Criando a linha central
    cv.line(cistercience_number, geom.points[1], geom.points[10], geom.color, geom.thickness)

    # Separando o numero
    m, c, d, u = split_digits(n)

    # Gerando unidade 1
    cistercience_number = unitLineGenerator(u, cistercience_number, {"color": geom.color, "thickness": geom.thickness})

    # Gerando unidade 10
    cistercience_number = centLineGenerator(d, cistercience_number, {"color": geom.color, "thickness": geom.thickness})

    # Gerando unidade 100
    cistercience_number = hundredLineGenerator(c, cistercience_number, {"color": geom.color, "thickness": geom.thickness})

    # Gerando unidade 10000
    cistercience_number = thousandLineGenerator(m, cistercience_number, {"color": geom.color, "thickness": geom.thickness})

    return cistercience_number, n

if __name__ == "__main__":

    number_c, original = generate_cistercience_number(input("Insira um numero entre 0 e 9999:\n"))
    cv.imshow(f"{original}:", number_c)
    k = cv.waitKey(0)