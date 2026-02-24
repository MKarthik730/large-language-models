from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ollama
from ddgs import DDGS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

def search_web(query: str):
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=3)
        snippets = [r["body"] for r in results]
        return "\n".join(snippets)

@app.post("/chat")
def chat(request: ChatRequest):
    # Search the web first
    search_results = search_web(request.message)

    # Pass search results as context to the model
    system_prompt = f"""You are a helpful assistant. 
Use the following web search results to answer the user's question accurately.

Web Search Results:
{search_results}

If the search results are not relevant, answer from your own knowledge."""

    response = ollama.chat(
    model="llama3.2",
    messages=[...],
    options={"num_predict": 150}  # limit response length
)   
    return {"response": response["message"]["content"]}