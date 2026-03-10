# Hệ Thống Truy Xuất Thông Tin Tài Liệu Khoa Học (NLP Information Retrieval)

## 1. Giới thiệu

Dự án này xây dựng một hệ thống **Information Retrieval (IR)** nhằm tìm
kiếm các bài báo khoa học trong lĩnh vực **Natural Language Processing
(NLP)**.

Mục tiêu của hệ thống:

- Thu thập và xử lý dữ liệu bài báo khoa học
- Xây dựng nhiều phương pháp truy xuất thông tin khác nhau
- So sánh hiệu năng giữa các phương pháp
- Đánh giá hệ thống bằng các **IR metrics** chuẩn

Ba nhóm phương pháp chính:

1.  Keyword-based Retrieval
2.  Embedding-based Retrieval
3.  Hybrid Retrieval

Mỗi nhóm bao gồm **hai phương pháp con** để so sánh hiệu quả.

---

# 2. Input / Output

## Input

Người dùng nhập một **query tìm kiếm**.

Ví dụ:

    transformer machine translation

## Output

Hệ thống trả về **Top-K bài báo liên quan nhất**.

Ví dụ:

    Top 5 Results

    1. Attention Is All You Need
    2. Transformer for Neural Machine Translation
    3. BERT: Pre-training of Deep Bidirectional Transformers
    4. T5: Exploring the Limits of Transfer Learning
    5. Scaling Transformers

Mỗi kết quả bao gồm:

- Title
- Authors
- Abstract
- Year
- Relevance score

---

# 3. Pipeline hệ thống

Pipeline tổng thể:

    Thu thập dữ liệu
          ↓
    Tiền xử lý dữ liệu
          ↓
    Xây dựng Index
          ↓
    Xử lý Query
          ↓
    Retrieval
          ↓
    Ranking
          ↓
    Top-K Results
          ↓
    Evaluation

Tùy chọn (demo):

    Top-K Results → LLM Summary → UI Demo

---

# 4. Dataset

Nguồn dữ liệu:

- arXiv API
- Các bài báo thuộc lĩnh vực NLP

Thông tin lưu trữ:

- id
- title
- abstract
- authors
- year
- category
- pdf_url

Cấu trúc dữ liệu:

    data/
        raw/
        processed/

---

# 5. Tiền xử lý dữ liệu

Các bước tiền xử lý văn bản:

### Text Cleaning

- chuyển về lowercase
- loại bỏ dấu câu
- loại bỏ ký tự đặc biệt

### Tokenization

Tách văn bản thành các token.

### Stopword Removal

Loại bỏ các từ phổ biến:

    the, is, are, for, and...

### Lemmatization / Stemming

Chuẩn hóa từ về dạng gốc.

Ví dụ:

    transformers → transformer
    models → model

---

# 6. Xây dựng Ground Truth

Ground truth dùng để đánh giá hệ thống.

Dạng dữ liệu:

    Query → Relevant Papers

Ví dụ:

    Query:
    machine translation transformer

    Relevant papers:
    - Attention Is All You Need
    - Transformer for Neural Machine Translation

## Query Set

Chuẩn bị khoảng **20--50 queries**.

Ví dụ:

    machine translation
    question answering
    text summarization
    information retrieval
    named entity recognition

## Synonym Queries

Một số query có từ đồng nghĩa:

    NLP ↔ natural language processing
    MT ↔ machine translation
    IR ↔ information retrieval

---

# 7. Các phương pháp Retrieval

## 7.1 Keyword-Based Retrieval

### Method 1: TF-IDF + Cosine Similarity

Biểu diễn văn bản bằng vector TF-IDF.

Độ tương đồng:

    cosine(query, document)

### Method 2: BM25

Thuật toán ranking phổ biến trong search engine.

Ưu điểm:

- xử lý tốt độ dài văn bản
- ranking chính xác hơn TF-IDF

---

## 7.2 Embedding-Based Retrieval

### Method 1: Sentence Embedding

Sử dụng mô hình Sentence-BERT để chuyển văn bản thành vector.

Sau đó tính **cosine similarity** giữa query và document.

### Method 2: Vector Search với FAISS

Sử dụng thư viện FAISS để xây dựng **vector index**.

Có thể sử dụng các thuật toán ANN:

- HNSW
- Product Quantization

---

## 7.3 Hybrid Retrieval

Kết hợp keyword search và semantic search.

### Method 1: Score Fusion

Kết hợp điểm số:

    final_score = α * BM25 + β * Embedding

### Method 2: Rank Fusion

Kết hợp thứ hạng của hai hệ thống.

Ví dụ:

    Reciprocal Rank Fusion (RRF)

---

# 8. Evaluation

Các chỉ số đánh giá:

### Precision@K

    Precision@5 = relevant_in_top5 / 5

### Recall@K

    Recall@5 = relevant_in_top5 / total_relevant_documents

### F1 Score

Trung bình điều hòa giữa Precision và Recall.

### MAP (Mean Average Precision)

Đánh giá chất lượng ranking trên nhiều queries.

---

# 9. Optional: LLM Integration

Sau khi retrieval, có thể sử dụng LLM để:

- tóm tắt nội dung bài báo
- so sánh các phương pháp
- tạo câu trả lời tự nhiên

LLM chỉ dùng **cho mục đích demo** và **không ảnh hưởng tới
evaluation**.

---

# 10. Cấu trúc Project

```
project/

    data/
        raw/                 # dữ liệu thu thập từ arXiv
        processed/           # dữ liệu sau preprocessing
        ground_truth/        # query + relevant documents

    notebooks/
        eda.ipynb
        keyword_retrieval.ipynb
        embedding_retrieval.ipynb
        hybrid_retrieval.ipynb

    src/

        data_pipeline/
            preprocessing.py
            dataset_loader.py

        keyword_retrieval/           # Nick
            build_inverted_index.py
            tfidf_retrieval.py
            bm25_retrieval.py
            keyword_pipeline.py

        embedding_retrieval/         # Khoa
            build_embedding_index.py
            sentence_embedding.py
            faiss_index.py
            embedding_pipeline.py

        hybrid_retrieval/            # Khoa
            score_fusion.py
            rank_fusion.py
            hybrid_pipeline.py

        evaluation/                  # Nick
            metrics.py
            evaluate_keyword.py
            evaluate_embedding.py
            evaluate_hybrid.py

    app/
        search_demo.py
        ui_demo.py

    experiments/
        run_keyword.py
        run_embedding.py
        run_hybrid.py

    README.md
    requirements.txt
```

---

# 11. Phân công công việc

## Nick Võ -- Data & Keyword Retrieval

Phụ trách:

### Data Pipeline

- preprocessing.py
- dataset_loader.py

### Retrieval Methods

- TF-IDF retrieval
- BM25 retrieval

### Evaluation

- Precision@K
- Recall@K
- MAP

---

## Anh Khoa -- Embedding & Hybrid Retrieval

Phụ trách:

### Ground Truth

- tạo tập query
- gán relevant documents

### Vector Retrieval

- Sentence-BERT embeddings
- FAISS vector index

### Hybrid Retrieval

- score fusion
- rank fusion

---

## Cả hai cùng thực hiện

- phân tích kết quả
- viết report
- xây dựng demo UI
- tích hợp LLM (optional)
