import faiss
import numpy as np
from src.retriever.embedding import E5FaissRetriever

def main():

    retriever = E5FaissRetriever()

    retriever.load("src/index/paper_index.faiss")
    retriever.doc_ids = np.load("src/index/doc_ids.npy")

    query = "transformer for information retrieval"

    results, scores = retriever.search(query, top_k=5)

    print(results)
    print(scores)

if __name__ == "__main__":
    main()