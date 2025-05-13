import cv2 as cv
import numpy as np

from Services.CistForge.types import ImageConfig

def unitLineGenerator(n: int, image: np.ndarray, pointBlocks: list[tuple[int, int]], image_configs: ImageConfig):
    match n:
        case 1:
            cv.line(image, pointBlocks[1], pointBlocks[2], image_configs["color"], image_configs["thickness"])
        case 2:
            cv.line(image, pointBlocks[4], pointBlocks[5], image_configs["color"], image_configs["thickness"])
        
    return image