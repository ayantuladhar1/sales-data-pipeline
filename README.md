# Sales Data Pipeline using Medallion Architecture

## 📌 Project Overview
This project demonstrates a mini end-to-end Data Engineering pipeline using the Medallion Architecture (Bronze → Silver → Gold).
The pipeline ingests raw sales data, cleans and transforms it using PySpark, and produces analytics-ready datasets stored in Parquet format and queried via Hive.

---

## 🏗 Architecture
Bronze → Silver → Gold

---

## 🛠 Tech Stack
- Python
- PySpark
- Apache Hive
- HDFS
- Parquet
- SQL

---

## 📂 Project Structure
**sales-data-pipeline/**
├── data/raw/sales.csv
├── src/
│ ├── ingest_bronze.py
│ ├── transform_silver.py
│ ├── load_gold.py
│ └── constants.py
├── hive/create_tables.sql
└── README.md


---

## 📄 Dataset
| Column | Description |
|------|------------|
| sale_id | Unique sale id |
| product_name | Product name |
| quantity | Units sold |
| price | Price per unit |
| sale_date | Date of sale |

---

## 🔄 Data Flow

### 🟤 Bronze Layer
- Raw CSV ingestion
- No transformations
- Stored as Parquet

### ⚪ Silver Layer
- Cleaned and typed data
- Ready for analytics

### 🟡 Gold Layer
- Aggregated sales metrics

---

## 🐍 How to Run

### Step – Bronze/Silver/Gold
```bash
spark-submit src/ingest_bronze.py
spark-submit src/transform_silver.py
spark-submit src/load_gold.py
