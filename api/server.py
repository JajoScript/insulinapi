import os
from fastapi import FastAPI, UploadFile, File, Request
from .models import predict
from aiofiles import open

app = FastAPI()

#* Middlewares
@app.middleware("http")
async def add_cors_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


#* Routes
@app.get("/")
async def Index():
    return {
        "message": "Estoy de pana banana 🍌"
    }


@app.post("/predecir")
async def PredecirFruta(request:Request, image: UploadFile=File(...)):
    # Guardar la imagen en el directorio image
    out_file_path = f"{os.getcwd()}\\api\\images\\{image.filename}"
    async with open(out_file_path, 'wb') as out_file:
            content = await image.read()
            await out_file.write(content)

    resultado = await predict.predecir_fruta(out_file_path)

    return {
        "fruta": resultado
    }
