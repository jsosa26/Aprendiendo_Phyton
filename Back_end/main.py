from fastapi import FastAPI

app = FasAPI()

@app.get("/")
async def root():
    return "Hola Mundo"