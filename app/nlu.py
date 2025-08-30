# Extracting the entities
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

class NLUModel:
    def __init__(self, model_name="d4data/biobert-base-cased-v1.1-ner"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForTokenClassification.from_pretrained(model_name)
        self.nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer, aggregation_strategy="simple")

    def extract_entities(self, query):
        ner_results = self.nlp(query)
        # Format entities as list of dicts with entity label and text span
        entities = [{"entity": ent["entity_group"], "text": ent["word"]} for ent in ner_results]
        return entities

# Example usage
if __name__ == "__main__":
    nlu = NLUModel()
    query = "What are the symptoms of diabetes and hypertension?"
    entities = nlu.extract_entities(query)
    print("Extracted Entities:", entities)
