from sentence_transformers import SentenceTransformer, util
import sqlite3
import numpy as np
import pickle

class Retriever:
    def __init__(self, db_path="data/med_corpus.db"):
        self.conn = sqlite3.connect(db_path)
        self.model = SentenceTransformer("pritamdeka/BioBERT-mnli-snli-scinli-scitail-mednli-stsb")

    def search(self, query, k=5):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, passage, embedding FROM passages")
        rows = cursor.fetchall()

        query_emb = self.model.encode([query], convert_to_tensor=True)
        passages = []
        embeddings = []
        for row in rows:
            passages.append(row[1])
            embeddings.append(pickle.loads(row[2]))

        embeddings = np.stack(embeddings)
        scores = util.cos_sim(query_emb, embeddings)[0]
        topk_indices = scores.topk(k).indices.cpu().tolist()

        return [passages[i] for i in topk_indices]
