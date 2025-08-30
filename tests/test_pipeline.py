from app.llm_ensemble import EnsembleLLM

def test_llm_basic():
    model = EnsembleLLM()
    res = model.generate("What is diabetes?")
    assert isinstance(res, list)
    assert len(res) > 0
