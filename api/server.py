from fastapi import FastAPI

app = FastAPI()

# * Routes.


@app.get("/")
async def Index():
    return {
        "message": "Estoy de pana banana 🍌"
    }
