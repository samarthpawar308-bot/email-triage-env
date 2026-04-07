from fastapi import FastAPI
from inference import main

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "running"}

@app.post("/reset")
async def reset():
    return {"status": "reset successful"}

@app.post("/step")
async def step():
    result = await main()
    return {"result": result}
