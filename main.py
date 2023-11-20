import uvicorn

# * Inicialización del servidor.
if (__name__ == "__main__"):
    print("[🐶] Iniciando la API ...")
    uvicorn.run(
        "api.server:app",
        reload=True
    )
