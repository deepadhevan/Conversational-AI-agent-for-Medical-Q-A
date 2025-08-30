from fastapi import FastAPI
from pydantic import BaseModel
from app.nlu import NLUModel
from app.retrieval import Retriever
from app.llm_ensemble import EnsembleLLM
from app.aggregator import aggregate
from fastapi.staticfiles import StaticFiles

app = FastAPI()

nlu = NLUModel()
retriever = Retriever()
ensemble = EnsembleLLM()

class Question(BaseModel):
    question: str

@app.post("/ask")
async def ask(q: Question):
    entities = nlu.extract_entities(q.question)
    docs = retriever.search(q.question)
    prompt = f"Question: {q.question}\nEvidence: {docs}"
    answers = ensemble.generate(prompt)
    final_answer = aggregate(answers)
    return {"answer": final_answer, "references": docs}

# Serve the UI static files
app.mount("/", StaticFiles(directory="static", html=True), name="static")
