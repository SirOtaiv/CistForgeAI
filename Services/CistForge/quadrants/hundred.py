import cv2 as cv
import numpy as np

from Services.CistForge.types import ImageConfig

def hundredLineGenerator(n: int, image: np.ndarray, pointBlocks: list[tuple[int, int]], image_configs: ImageConfig):
    match n:
        case 1:
            cv.line(image, pointBlocks[10], pointBlocks[11], image_configs["color"], image_configs["thickness"])

        case 2:
            cv.line(image, pointBlocks[7], pointBlocks[8], image_configs["color"], image_configs["thickness"])

        case 3:
            cv.line(image, pointBlocks[10], pointBlocks[8], image_configs["color"], image_configs["thickness"])

        case 4:
            cv.line(image, pointBlocks[7], pointBlocks[11], image_configs["color"], image_configs["thickness"])

        case 5:
            cv.line(image, pointBlocks[7], pointBlocks[11], image_configs["color"], image_configs["thickness"])
            cv.line(image, pointBlocks[10], pointBlocks[11], image_configs["color"], image_configs["thickness"])

        case 6:
            cv.line(image, pointBlocks[8], pointBlocks[11], image_configs["color"], image_configs["thickness"])

        case 7:
            cv.line(image, pointBlocks[8], pointBlocks[11], image_configs["color"], image_configs["thickness"])
            cv.line(image, pointBlocks[10], pointBlocks[11], image_configs["color"], image_configs["thickness"])

        case 8:
            cv.line(image, pointBlocks[7], pointBlocks[8], image_configs["color"], image_configs["thickness"])
            cv.line(image, pointBlocks[8], pointBlocks[11], image_configs["color"], image_configs["thickness"])

        case 9:
            cv.line(image, pointBlocks[7], pointBlocks[8], image_configs["color"], image_configs["thickness"])
            cv.line(image, pointBlocks[8], pointBlocks[11], image_configs["color"], image_configs["thickness"])
            cv.line(image, pointBlocks[10], pointBlocks[11], image_configs["color"], image_configs["thickness"])
        
    return image