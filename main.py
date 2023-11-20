import uvicorn

# * Inicialización del servidor.
if (__name__ == "__main__"):
    print("[🐶] Iniciando la API ...")
    PORT = 8023

    configuration = uvicorn.Config(
        "api.server:app",
        port=PORT,

        reload=True,
        reload_delay=1000,

        log_level="debug"
    )
    server = uvicorn.Server(configuration)

    server.run()

