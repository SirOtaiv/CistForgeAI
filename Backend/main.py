from typing import Union

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from Backend.services.generate_service import generate_image_serv

app = FastAPI(
    title="Cisterciense Portal - Backend",
    description="Backend for Cisterciense Numbers",
    version="1.0.0"
    )


@app.get("/", tags=["General"])
def read_root():
    return {"Hello": "World"}

@app.post("/image/{number}", tags=["Image Generator"])
def generate_cistcer_number(number: int):
    image_return = generate_image_serv(number)
    return StreamingResponse(image_return, media_type="image/png")