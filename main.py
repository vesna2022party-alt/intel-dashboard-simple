from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/regions")
def regions():
    return [
        {"region":"Kyiv","risk":0.8},
        {"region":"Lviv","risk":0.4},
        {"region":"Kharkiv","risk":0.9},
        {"region":"Odesa","risk":0.7}
    ]
