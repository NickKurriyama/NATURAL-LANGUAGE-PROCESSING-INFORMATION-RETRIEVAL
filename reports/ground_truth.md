# Ground Truth Construction Report

**Project:** Scientific Paper Information Retrieval  
**Data Source:** arXiv (2015–2025)

---

# 1. Corpus Construction

## Data Source

Corpus được xây dựng từ **arXiv metadata dataset**, bao gồm các bài báo khoa học trong giai đoạn **2015–2025**.

## Processing Pipeline

Dữ liệu thô được lưu dưới dạng nhiều file `jsonl`.  
Mỗi dòng tương ứng với metadata của một paper.

Quy trình xử lý:

1. Đọc toàn bộ file `jsonl` trong thư mục dữ liệu.
2. Parse từng dòng JSON.
3. Loại bỏ paper trùng `id`.
4. Trích xuất các trường cần thiết:
   - `id`
   - `title`
   - `abstract`
   - `authors`
   - `categories`
   - `update_date`

## Output Dataset

Sau khi xử lý, dữ liệu được lưu thành:

```
papers_2015_2025.parquet
```

Cấu trúc mỗi record:

```
{
  id
  title
  abstract
  authors
  categories
  update_date
}
```

Dataset này đóng vai trò **document corpus** cho hệ thống Information Retrieval.

---

# 2. Query Generation

Do không có query log thực tế, chúng tôi tạo **synthetic queries** dựa trên các chủ đề phổ biến trong lĩnh vực NLP và Information Retrieval.

## Query Topics

Danh sách topic được thiết kế từ các hướng nghiên cứu phổ biến:

- neural machine translation
- information retrieval
- document ranking
- transformer language models
- contrastive learning
- question answering
- document retrieval
- large language models
- multilingual NLP
- neural search
- dense passage retrieval
- scientific paper recommendation
- semantic similarity
- knowledge graph reasoning
- self supervised learning
- text classification
- topic modeling
- document clustering
- neural reranking
- representation learning
- language understanding
- cross lingual retrieval
- neural embeddings

Ngoài ra còn bổ sung:

**Task modifiers**

- models
- methods
- techniques
- algorithms
- systems

**Context phrases**

- for academic search
- for scientific papers
- for research literature
- in neural IR systems
- for multilingual corpora
- in academic recommender systems

---

# 3. Query Length Distribution

Để mô phỏng hành vi tìm kiếm thực tế, độ dài query được phân bố như sau:

| Query Length | Count |
|---------------|-------|
| 1 word | 35 |
| 2 words | 60 |
| 3 words | 90 |
| 4 words | 60 |
| 5 words | 35 |
| 6 words | 20 |

Tổng cộng:

```
300 queries
```

---

# 4. Query Diversity Control

Để tránh các query quá giống nhau, chúng tôi sử dụng **token overlap filtering**.

Similarity metric:

```
overlap = |tokens(q1) ∩ tokens(q2)| / |tokens(q1) ∪ tokens(q2)|
```

Nếu:

```
overlap ≥ 0.5
```

query mới sẽ bị loại và sinh lại.

Cơ chế này giúp:

- Tăng **đa dạng semantic**
- Giảm **duplicate queries**

---

# 5. Query Dataset

Queries được lưu dưới dạng:

```
queries.parquet
```

Schema:

```
query_id
text
```

Ví dụ:

```
q1  neural machine translation
q2  transformer language models
q3  document ranking methods
```

---

# 6. Ground Truth Construction (Qrels)

Ground truth relevance được tạo bằng cách truy vấn **arXiv API**.

## Retrieval Procedure

Với mỗi query:

1. Gửi truy vấn tới:

```
http://export.arxiv.org/api/query
```

2. Tìm kiếm trong field:

```
abstract
```

3. Kết quả được:

```
sortBy=relevance
```

4. Thu thập tối đa:

```
TOP_K = 50 documents
```

---

# 7. Filtering Conditions

Các document phải thỏa mãn các điều kiện sau.

## Year constraint

```
2015 ≤ year ≤ 2025
```

## Category constraint

Chỉ giữ các lĩnh vực:

```
cs.AI
cs.CL
cs.IR
cs.LG
```

## Corpus alignment

Document phải tồn tại trong corpus đã xây dựng.

Điều này đảm bảo:

```
qrels ⊂ corpus
```

---

# 8. Relevance Labeling Strategy

Do arXiv API trả kết quả đã được **rank theo relevance**, chúng tôi chuyển thứ hạng thành **graded relevance labels**.

| Rank | Relevance |
|-----|-----------|
| 1–6 | 3 (Highly relevant) |
| 7–21 | 2 (Relevant) |
| 22–50 | 1 (Weakly relevant) |

Việc sử dụng graded relevance cho phép đánh giá bằng các metric như:

- nDCG
- MAP
- Recall@K
- Precision@K

---

# 9. Final Ground Truth Dataset

Dataset ground truth gồm hai thành phần.

## Queries

```
queries.parquet
```

## Relevance Judgments

```
qrels.parquet
```

Schema:

```
query_id
doc_id
relevance
```

---

# 10. Pipeline Overview

Toàn bộ pipeline xây dựng ground truth:

```
arXiv metadata
      ↓
Corpus construction
      ↓
Query generation
      ↓
arXiv API retrieval
      ↓
Filtering
(year + category + corpus)
      ↓
Rank → relevance mapping
      ↓
Ground truth (qrels)
```

---

# 11. Advantages

### Realistic queries
Queries được xây dựng dựa trên các **research topics phổ biến trong NLP**.

### Query diversity
Áp dụng **token overlap filtering** để giảm trùng lặp.

### Reliable relevance
Relevance labels được suy ra từ **arXiv relevance ranking**.

### Corpus consistency
Mọi document trong qrels đều tồn tại trong corpus.

---

# 12. Output Files

```
data/
 ├── raw/
 │   └── papers_2015_2025.parquet
 │
 └── ground_truth/
     ├── queries.parquet
     └── qrels.parquet
```