from fastapi import FastAPI
from pydantic import BaseModel
from calc import calculate_dc

app = FastAPI()

class Input(BaseModel):
    racks: int
    kw_per_rack: float

@app.get("/")
def root():
    return {"message": "Smart POD API Running"}

@app.post("/calculate")
def calculate(data: Input):
    return calculate_dc(data.racks, data.kw_per_rack)
