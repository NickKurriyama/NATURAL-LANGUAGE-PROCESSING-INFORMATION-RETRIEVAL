import faiss
import numpy as np
import torch
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

class E5FaissRetriever:

    def __init__(self, model_name="intfloat/e5-base", device=None, cache_dir="../models/e5-base"):

        self.device = device if device else (
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        self.model = SentenceTransformer(model_name, 
                                         device=self.device,
                                         cache_folder=cache_dir)
        self.index = None
        self.doc_ids = None

    def encode_documents(self, texts, batch_size=128):

        texts = ["passage: " + t for t in texts]

        embeddings = []

        for i in tqdm(range(0, len(texts), batch_size), desc="Encoding docs"):
            batch = texts[i:i+batch_size]

            emb = self.model.encode(
                batch,
                convert_to_numpy=True,
                normalize_embeddings=True,
                show_progress_bar=False
            )

            embeddings.append(emb)

        return np.vstack(embeddings)

    def encode_queries(self, queries):

        queries = ["query: " + q for q in queries]

        emb = self.model.encode(
            queries,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return emb

    def build_index(self, embeddings, doc_ids):

        embeddings = embeddings.astype("float32")

        dim = embeddings.shape[1]

        index = faiss.IndexHNSWFlat(dim, 32, faiss.METRIC_INNER_PRODUCT)

        index.hnsw.efConstruction = 200
        index.hnsw.efSearch = 128

        index.add(embeddings)

        self.index = index
        self.doc_ids = np.array(doc_ids)

    def search(self, query, top_k=10):

        q_emb = self.encode_queries([query])

        scores, indices = self.index.search(q_emb, top_k)

        results = self.doc_ids[indices[0]]

        return results, scores[0]

    def save(self, path):

        faiss.write_index(self.index, path)

    def load(self, path):

        self.index = faiss.read_index(path)