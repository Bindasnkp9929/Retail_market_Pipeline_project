# 🛒 RetailMart Data Pipeline

A simple **Data Engineering** project built using **Python, Pandas, NumPy, and SQLite** to clean, transform, and analyze retail sales data. This project demonstrates a complete ETL (Extract, Transform, Load) pipeline by processing raw CSV files and generating meaningful business insights.

---

## 📌 Project Overview

RetailMart Pvt. Ltd. collects daily sales data from multiple stores across India. The raw data contains missing values, duplicate records, and inconsistent formats.

This project performs:

* Data Ingestion
* Data Cleaning
* Data Transformation
* Data Loading into SQLite
* SQL Analysis
* Business Reporting
* Error Handling

---

## 📂 Project Structure

```text
Retailmart_data_pipeline/
│── sales_data.csv
│── products.csv
│── stores.csv
│── pipeline.py
│── retail_sales.db
│── README.md
```

---

## 🚀 Features

* Load multiple CSV files using Pandas
* Detect and handle missing values
* Remove duplicate records
* Convert incorrect data types
* Merge datasets using JOIN operations
* Calculate total revenue
* Generate city-wise revenue reports
* Load processed data into SQLite
* Execute SQL queries for business insights
* Generate summary reports
* Complete ETL pipeline using a single function
* Basic error handling using try-except

---

## 🛠️ Technologies Used

* Python 3
* Pandas
* NumPy
* SQLite3

---

## 📊 Dataset

### sales_data.csv

Contains daily sales transactions.

Columns:

* sale_id
* store_id
* product_id
* quantity
* sale_date
* amount

### products.csv

Contains product information.

Columns:

* product_id
* product_name
* category
* price

### stores.csv

Contains store details.

Columns:

* store_id
* store_name
* city
* region

---

## ⚙️ Pipeline Workflow

### 1. Data Ingestion

* Load CSV files
* Display dataset shape
* Display first five records
* Check missing values

### 2. Data Cleaning

* Remove duplicate rows
* Fill missing quantity values
* Remove rows with missing amount
* Convert data types

### 3. Data Transformation

* Merge all datasets
* Calculate Total Revenue
* Generate revenue statistics
* Calculate city-wise revenue

### 4. Data Loading

* Create SQLite database
* Store cleaned dataset into `retail_sales` table

### 5. SQL Reporting

* Top 3 best-selling products
* Total revenue per store per day

### 6. Summary Report

Displays:

* Total Transactions
* Total Revenue
* Top Selling City
* Top Selling Product

---

## 📈 SQL Queries

### Top 3 Best Selling Products

```sql
SELECT product_name,
SUM(quantity) AS total_quantity
FROM retail_sales
GROUP BY product_name
ORDER BY total_quantity DESC
LIMIT 3;
```

### Revenue Per Store Per Day

```sql
SELECT store_name,
sale_date,
SUM(total_revenue) AS total_revenue
FROM retail_sales
GROUP BY store_name, sale_date
ORDER BY sale_date;
```

---

## ▶️ How to Run

### Install Dependencies

```bash
pip install pandas numpy
```

### Run the Project

```bash
python pipeline.py
```

---

## 📋 Output

The pipeline will generate:

* Cleaned dataset
* Revenue statistics
* City-wise revenue
* SQLite database (`retail_sales.db`)
* SQL query results
* Business summary report

---

## 📸 Sample Output

```
Pipeline executed successfully!

Total Transactions : 18

Total Revenue : 31250

Top Selling City : Delhi

Top Selling Product : Laptop
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* ETL Pipeline Development
* Data Cleaning using Pandas
* Data Transformation
* SQL Database Integration
* SQL Querying
* Business Intelligence Reporting
* Exception Handling in Python

---

## 👨‍💻 Author

**Nitesh Kumar Prajapat**

B.Tech Student | Data Engineering & Python Enthusiast

---

## ⭐ If you found this project useful, consider giving it a Star on GitHub!
