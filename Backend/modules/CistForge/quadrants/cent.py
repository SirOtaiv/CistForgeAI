import cv2 as cv
import numpy as np

from Backend.modules.CistForge.geometry import geometry_points_generate
from Backend.modules.CistForge.types import ImageConfig

def centLineGenerator(n: int, image: np.ndarray, image_configs: ImageConfig):

    geom = geometry_points_generate()

    match n:
        case 1:
            cv.line(image, geom.points[0], geom.points[1], image_configs["color"], image_configs["thickness"])

        case 2:
            cv.line(image, geom.points[4], geom.points[3], image_configs["color"], image_configs["thickness"])

        case 3:
            cv.line(image, geom.points[1], geom.points[3], image_configs["color"], image_configs["thickness"])

        case 4:
            cv.line(image, geom.points[4], geom.points[0], image_configs["color"], image_configs["thickness"])

        case 5:
            cv.line(image, geom.points[1], geom.points[0], image_configs["color"], image_configs["thickness"])
            cv.line(image, geom.points[4], geom.points[0], image_configs["color"], image_configs["thickness"])

        case 6:
            cv.line(image, geom.points[0], geom.points[3], image_configs["color"], image_configs["thickness"])

        case 7:
            cv.line(image, geom.points[1], geom.points[0], image_configs["color"], image_configs["thickness"])
            cv.line(image, geom.points[0], geom.points[3], image_configs["color"], image_configs["thickness"])

        case 8:
            cv.line(image, geom.points[4], geom.points[3], image_configs["color"], image_configs["thickness"])
            cv.line(image, geom.points[3], geom.points[0], image_configs["color"], image_configs["thickness"])

        case 9:
            cv.line(image, geom.points[4], geom.points[3], image_configs["color"], image_configs["thickness"])
            cv.line(image, geom.points[3], geom.points[0], image_configs["color"], image_configs["thickness"])
            cv.line(image, geom.points[1], geom.points[0], image_configs["color"], image_configs["thickness"])
        
    return image