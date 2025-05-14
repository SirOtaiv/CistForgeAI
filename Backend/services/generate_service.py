import io
import cv2 as cv

from Backend.modules.CistForge.main import generate_cistercience_number

def generate_image_serv(number: int):
    # Gera a imagem consumindo o serviço
    image_np, _ = generate_cistercience_number(number)

    # Converte para png
    _, img_encoded = cv.imencode('.png',image_np)
    img_bytes = io.BytesIO(img_encoded.tobytes())

    # Retornando como bites
    return img_bytes