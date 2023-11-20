from fastapi import FastAPI
from .models import predict

app = FastAPI()

#* Routes
@app.get("/")
async def Index():
    return {
        "message": "Estoy de pana banana 🍌"
    }


@app.post("/predecir")
async def PredecirFruta():
    resultado = await predict.predecir_fruta()

    return {
        "message": resultado
    }
