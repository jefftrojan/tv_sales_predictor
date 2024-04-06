from fastapi import FastAPI, status
import nest_asyncio
from pyngrok import ngrok
import uvicorn
from pydantic import BaseModel, Field
from model import predict

app = FastAPI()

class RequestModel(BaseModel):
    tv: float = Field(gt=0, lt=10000)

@app.get('/')
async def home():
    return "Hello World"

@app.post('/predict', status_code=status.HTTP_200_OK)
async def predict_fast_api(request: RequestModel):
    value = request.tv
    predicted_value = predict(value)
    return f'Predicted Tv sales : {predicted_value}'

async def main():
    config = uvicorn.Config(app)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())