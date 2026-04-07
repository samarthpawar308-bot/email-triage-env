from fastapi import FastAPI
from inference import main as run_main

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "running"}

@app.post("/reset")
async def reset():
    return {"status": "reset successful"}

@app.post("/step")
async def step():
    result = await run_main()
    return {"result": result}

# ✅ REQUIRED by OpenEnv
def main():
    return app

# ✅ REQUIRED (entry point)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)
