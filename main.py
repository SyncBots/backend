from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# ***** CORS Middleware ***** #
# This will allow all origins to access the API.
# Why do we need CORSMiddleware?
# In order to make cross-origin requests forma  different port
# you need to enable Cross Origin Resource Sharing (CORS).
# FastAPI's built-in CORSMiddleware handles this for us.
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "SUCCESS: You got the root GET"}

