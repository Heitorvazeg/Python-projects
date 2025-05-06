import openai
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_methods=["POST"],
    allow_headers = ["*"],
)

@app.post("/chat")
async def chat(data: dict):
    message = data.get("message")

    response = openai.ChatCompletion.create(
        model="gpt-",
        messages = [{"role":"user", "content": message}]
    )

    return {"reply": response["choices"][0]["message"]["content"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)