from typing import Union

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, StreamingResponse

from Backend.services.generate_service import generate_image_serv

app = FastAPI(
    title="Cisterciense Portal - Backend",
    description="Backend for Cisterciense Numbers",
    version="1.0.0"
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error_message": exc.detail}
    )

@app.get("/", tags=["General"])
def read_root():
    return {"Hello": "World"}

@app.post("/image-generate/", tags=["Image"])
def generate_cistcer_number(number: int):
    if number > 9999:
        raise HTTPException(status_code=400, detail="O número é maior que o permitido. O valor máximo é 9999.")
    if number < 1:
        raise HTTPException(status_code=400, detail="O número deve ser maior ou igual a 1.")
    image_return = generate_image_serv(number)
    return StreamingResponse(image_return, media_type="image/png")