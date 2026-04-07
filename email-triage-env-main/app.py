from fastapi import FastAPI
import asyncio
from inference import main

app = FastAPI()

@app.get("/")
async def run_env():
    await main()
    return {"status": "Environment ran successfully"}
