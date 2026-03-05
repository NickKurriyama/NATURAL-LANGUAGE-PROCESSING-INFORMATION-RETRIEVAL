
# Hệ Thống Truy Xuất Thông Tin Tài Liệu Khoa Học (NLP-IR)

## 1. Introduction

Dự án này xây dựng một hệ thống **Natural Language Processing
Information Retrieval (NLP‑IR)** nhằm tìm kiếm và tổng hợp thông tin từ
tập lớn các bài báo khoa học liên quan đến xử lý ngôn ngữ tự nhiên.

Hệ thống cho phép người dùng nhập:

-   **Query**: chủ đề cần tìm kiếm\
-   **Prompt**: yêu cầu cách trả lời (tóm tắt, so sánh, liệt kê phương pháp)

Và sinh ra các kết quả:

1.  Tìm các bài báo liên quan
2.  Xếp hạng theo mức độ liên quan
3.  Sinh câu trả lời tổng hợp bằng ngôn ngữ tự nhiên

------------------------------------------------------------------------

## 2. Input / Output

### Input

-   Query: nội dung người dùng muốn tìm
-   Prompt: yêu cầu định dạng câu trả lời

Ví dụ:

Query: transformer for machine translation\
Prompt: summarize methods

### Output

-   Câu trả lời tổng hợp
-   Danh sách các bài báo liên quan

Ví dụ:

Answer: Tóm tắt các phương pháp sử dụng mô hình Transformer trong dịch
máy.

Relevant papers: 1. Attention Is All You Need 2. BERT: Pre‑training of
Deep Bidirectional Transformers 3. T5: Exploring the Limits of Transfer
Learning

------------------------------------------------------------------------

## 3. Pipeline hệ thống

Data Collection\
→ Preprocessing\
→ Indexing\
→ Query Processing\
→ Search & Ranking\
→ Answer Generation\
→ Evaluation

------------------------------------------------------------------------

## 4. Thu thập dữ liệu

Nguồn dữ liệu chính:

-   arXiv API
-   PDF papers
-   Metadata của bài báo

Thông tin lưu trữ:

-   title
-   authors
-   abstract
-   year
-   category
-   pdf

------------------------------------------------------------------------

## 5. Tiền xử lý dữ liệu

Bài báo khoa học thường có các đặc điểm:

-   bố cục nhiều cột
-   công thức toán học
-   bảng biểu và hình ảnh
-   danh sách tài liệu tham khảo

### 5.1 Trích xuất text từ PDF

Các thư viện có thể sử dụng:

-   PyMuPDF
-   pdfplumber
-   GROBID
-   Nougat

### 5.2 Trích xuất cấu trúc bài báo

Các phần quan trọng:

-   Abstract
-   Introduction
-   Related Work
-   Methodology
-   Experiments
-   Conclusion
-   References

### 5.3 Xử lý văn bản

Các bước NLP:

-   Tokenization
-   Stopword Removal
-   Lemmatization / Stemming
-   Text Normalization

------------------------------------------------------------------------

## 6. Lập chỉ mục (Indexing)

Hệ thống sử dụng **Inverted Index** để tìm kiếm nhanh.

Ví dụ:

transformer → \[paper1, paper5, paper8\]\
attention → \[paper2, paper4, paper5\]\
bert → \[paper3, paper7\]

------------------------------------------------------------------------

## 7. Xử lý truy vấn (Query Processing)

Các bước:

1.  Tokenization
2.  Loại bỏ stopwords
3.  Mở rộng từ đồng nghĩa
4.  Dịch query nếu nhập bằng tiếng Việt

Ví dụ:

Query: "mô hình transformer cho dịch máy"

→ dịch sang:

"transformer model for machine translation"

------------------------------------------------------------------------

## 8. Search và Ranking

### Retrieval

Các phương pháp:

-   BM25
-   Boolean Search
-   Cosine Similarity

Hệ thống trả về **Top‑K papers** có liên quan nhất.

### Ranking

Danh sách Top‑K được xếp hạng lại theo độ liên quan.

------------------------------------------------------------------------

## 9. Sinh câu trả lời (Answer Generation)

Hệ thống tổng hợp nội dung từ các bài báo:

-   tóm tắt nội dung
-   so sánh phương pháp
-   liệt kê các kỹ thuật
-   trả lời câu hỏi theo prompt

Ví dụ:

Prompt: compare methods

Output: So sánh giữa Transformer, BERT và T5.

------------------------------------------------------------------------

## 10. Đánh giá hệ thống

Các chỉ số đánh giá:

-   Precision
-   Recall
-   F1 Score
-   MAP (Mean Average Precision)

Những chỉ số này đánh giá mức độ chính xác của hệ thống tìm kiếm.

------------------------------------------------------------------------

## 11. Cấu trúc project

project/

data/ - raw_papers - processed_papers

src/ - data_collection.py - pdf_extraction.py - preprocessing.py -
indexing.py - retrieval.py - query_processing.py - ranking.py -
answer_generation.py - evaluation.py

app/ - main.py

requirements.txt\
README.md

------------------------------------------------------------------------
## Giới thiệu
Dự án xây dựng hệ thống tìm kiếm và tổng hợp thông tin từ các bài báo khoa học sử dụng NLP và Information Retrieval.

## Pipeline
Data Collection → Preprocessing → Indexing → Query Processing → Search & Ranking → Answer Generation → Evaluation

## Scheduling

### Member 1 – Data Pipeline
- data_collection.py
- pdf_extraction.py
- preprocessing.py
- indexing.py
- retrieval.py

### Member 2 – Query & Answer System
- query_processing.py
- ranking.py
- answer_generation.py
- evaluation.py
- main.py
