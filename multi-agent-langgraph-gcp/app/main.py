from fastapi import FastAPI
from pydantic import BaseModel
from app.graph import build_graph

app = FastAPI()
graph = build_graph()

class Request(BaseModel):
    dataset: str

@app.post("/run")
def run_agent(request: Request):
    state = {
        "dataset": request.dataset,
        "profile": None,
        "analysis": None,
        "model": None
    }

    result = graph.invoke(state)
    return result