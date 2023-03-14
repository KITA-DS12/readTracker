from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test1")
async def test1(name: str = ""):
    return {"message": name}


@app.get("/test2/{name}")
async def test2(name: str = ""):
    return {"message": name}


class User(BaseModel):
    name: str


@app.post("/test3")
async def test3(user: User):
    return {"message": user.name}

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        reload=True,
        port=8888,
        log_level="debug"
    )
