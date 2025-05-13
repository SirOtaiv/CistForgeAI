import cv2 as cv
import numpy as np

from Services.CistForge.geometry import geometry_points_generate
from Services.CistForge.types import ImageConfig

def thousandLineGenerator(n: int, image: np.ndarray, image_configs: ImageConfig):

    geom = geometry_points_generate()

    match n:
        case 1:
            cv.line(image, geom.points[9], geom.points[10], image_configs["color"], image_configs["thickness"])

        case 2:
            cv.line(image, geom.points[6], geom.points[7], image_configs["color"], image_configs["thickness"])

        case 3:
            cv.line(image, geom.points[10], geom.points[6], image_configs["color"], image_configs["thickness"])

        case 4:
            cv.line(image, geom.points[9], geom.points[7], image_configs["color"], image_configs["thickness"])

        case 5:
            cv.line(image, geom.points[9], geom.points[7], image_configs["color"], image_configs["thickness"])
            cv.line(image, geom.points[9], geom.points[10], image_configs["color"], image_configs["thickness"])

        case 6:
            cv.line(image, geom.points[6], geom.points[9], image_configs["color"], image_configs["thickness"])

        case 7:
            cv.line(image, geom.points[6], geom.points[9], image_configs["color"], image_configs["thickness"])
            cv.line(image, geom.points[9], geom.points[10], image_configs["color"], image_configs["thickness"])

        case 8:
            cv.line(image, geom.points[6], geom.points[7], image_configs["color"], image_configs["thickness"])
            cv.line(image, geom.points[6], geom.points[9], image_configs["color"], image_configs["thickness"])

        case 9:
            cv.line(image, geom.points[6], geom.points[7], image_configs["color"], image_configs["thickness"])
            cv.line(image, geom.points[6], geom.points[9], image_configs["color"], image_configs["thickness"])
            cv.line(image, geom.points[9], geom.points[10], image_configs["color"], image_configs["thickness"])
        
    return image