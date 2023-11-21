import os
from fastapi import FastAPI, UploadFile, File
from .models import predict
from aiofiles import open

app = FastAPI()

#* Routes
@app.get("/")
async def Index():
    return {
        "message": "Estoy de pana banana 🍌"
    }


@app.post("/predecir")
async def PredecirFruta(image: UploadFile=File(...)):
    # Guardar la imagen en el directorio image
    out_file_path = f"{os.getcwd()}\\api\\images\\{image.filename}"
    async with open(out_file_path, 'wb') as out_file:
            content = await image.read()
            await out_file.write(content)

    resultado = await predict.predecir_fruta(out_file_path)

    return {
        "fruta": resultado
    }
