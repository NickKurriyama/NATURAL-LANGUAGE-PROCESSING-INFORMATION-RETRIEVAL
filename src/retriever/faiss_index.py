import numpy as np
from src.data.preprocess import PaperPreprocessor
from src.retriever.embedding import E5FaissRetriever

def main():

    processor = PaperPreprocessor()
    retriever = E5FaissRetriever()

    df = processor.preprocess_dataset(
        "data/raw/papers_2015_2025.parquet", "data/preprocessed/emb_base.parquet"
    )

    print("Encoding documents...")

    embeddings = retriever.encode_documents(
        df["text"].tolist()
    )

    print("Building FAISS index...")

    retriever.build_index(
        embeddings,
        df["doc_id"].tolist()
    )

    retriever.save("src/index/paper_index.faiss")

    np.save("src/index/doc_ids.npy", df["doc_id"].values)

    print("Done.")
    
if __name__ == "__main__":
    main()