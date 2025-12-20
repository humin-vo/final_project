from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app = FastAPI()

class Item(BaseModel):
    name: str
    phone_number: str

# endpoint functions
@app.get("/hello")
def read_root():
    return {"message": "Hello world"}

@app.get("/minh")
def read_root():
    y = 1 + 1
    return {"message": y}

@app.post("/items")
def create_item(item: Item):
    return {"item": item}

# start the server
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8001,
        reload=True
    )
    