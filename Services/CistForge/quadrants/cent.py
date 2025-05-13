import cv2 as cv
import numpy as np

from Services.CistForge.types import ImageConfig

def centLineGenerator(n: int, image: np.ndarray, pointBlocks: list[tuple[int, int]], image_configs: ImageConfig):
    match n:
        case 1:
            cv.line(image, pointBlocks[0], pointBlocks[1], image_configs["color"], image_configs["thickness"])

        case 2:
            cv.line(image, pointBlocks[4], pointBlocks[3], image_configs["color"], image_configs["thickness"])

        case 3:
            cv.line(image, pointBlocks[1], pointBlocks[3], image_configs["color"], image_configs["thickness"])

        case 4:
            cv.line(image, pointBlocks[4], pointBlocks[0], image_configs["color"], image_configs["thickness"])

        case 5:
            cv.line(image, pointBlocks[1], pointBlocks[0], image_configs["color"], image_configs["thickness"])
            cv.line(image, pointBlocks[4], pointBlocks[0], image_configs["color"], image_configs["thickness"])

        case 6:
            cv.line(image, pointBlocks[0], pointBlocks[3], image_configs["color"], image_configs["thickness"])

        case 7:
            cv.line(image, pointBlocks[1], pointBlocks[0], image_configs["color"], image_configs["thickness"])
            cv.line(image, pointBlocks[0], pointBlocks[3], image_configs["color"], image_configs["thickness"])

        case 8:
            cv.line(image, pointBlocks[4], pointBlocks[3], image_configs["color"], image_configs["thickness"])
            cv.line(image, pointBlocks[3], pointBlocks[0], image_configs["color"], image_configs["thickness"])

        case 9:
            cv.line(image, pointBlocks[4], pointBlocks[3], image_configs["color"], image_configs["thickness"])
            cv.line(image, pointBlocks[3], pointBlocks[0], image_configs["color"], image_configs["thickness"])
            cv.line(image, pointBlocks[1], pointBlocks[0], image_configs["color"], image_configs["thickness"])
        
    return image