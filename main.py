import fastapi
import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title='New API',
    description= 'API created with FASTAPI',
    version='0.1.0'
)

@app.get('/')
async def root():

    """
    Root endpoint
    
    """
    return {"mensaje": "Welcome to my FastAPI API"}