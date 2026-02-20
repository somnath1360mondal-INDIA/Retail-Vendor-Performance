# 📊 Vendor Performance Data Analytics

An end-to-end retail analytics project focused on improving profitability, pricing strategy, and vendor decision-making through data engineering, exploratory analysis, and business intelligence dashboards.

---

## 🚀 Project Overview

Retail businesses often struggle with slow-moving inventory, inconsistent vendor performance, and pricing strategies that negatively impact margins.
This project analyzes **sales, purchasing, freight cost, and vendor data** to generate actionable insights that help improve operational efficiency and business profitability.

The solution combines:

* Automated **Python data pipelines**
* SQL database modeling
* Exploratory Data Analysis (EDA)
* Interactive **Power BI dashboards**

---

## 🎯 Objectives

* Identify underperforming brands requiring pricing or inventory adjustments
* Determine top-performing vendors driving revenue and gross profit
* Analyze how bulk purchasing affects unit cost and margins
* Compare high vs low performing vendors to assess supplier dependency risks
* Provide executive-level business health insights

---

## 🏗️ Project Architecture

### 1️⃣ Data Engineering

* Built automated database creation scripts using:

  * `pandas`
  * `SQLAlchemy`
  * `sqlite`
* Implemented logging and exception handling for reliable data pipelines
* Created consolidated analytical tables combining:

  * Purchases
  * Purchase Prices
  * Vendor Invoices (Freight)
  * Sales

### 2️⃣ Exploratory Data Analysis (EDA)

* Validated table relationships and data flow
* Used weighted averages for purchase price aggregation
* Designed vendor-brand level profitability metrics

### 3️⃣ Data Modeling

Created a final analytics table containing:

* Purchase Quantity & Cost
* Freight Cost
* Sales Quantity & Revenue
* Profitability KPIs
* Vendor & Brand performance indicators

### 4️⃣ Power BI Dashboard

Interactive dashboards include:

* 📌 **Vendor & Brand Performance Overview**
* 📉 **Underperforming Brands Analysis**
* 🏆 **Top Performing Vendors**
* 📦 **Performance Based on Purchase Quantity**
* ⚖️ **High vs Low Performing Vendors**
* 🧠 **Business Health Summary**

---

## 📊 Key Insights

* Several brands generate negative profit despite strong revenue.
* Freight cost significantly impacts margins.
* Bulk purchasing generally improves unit economics and profitability.
* Vendor dependency risk exists due to heavy reliance on a few high performers.

---

## 🛠️ Tech Stack

**Languages & Tools**

* Python
* SQL / SQLite
* Power BI

**Libraries**

* pandas
* sqlalchemy
* os

---

## 📂 Repository Structure

```
├── data/                 # Raw or processed datasets
├── scripts/              # Automated data pipeline scripts
├── notebooks/            # EDA and analysis notebooks
├── powerbi/              # Power BI report files
├── database/             # SQLite database
└── README.md
```

---

## ⚙️ How to Run

1. Clone the repository

```
git clone https://github.com/yourusername/vendor-performance-analytics.git
```

2. Install dependencies

```
pip install pandas sqlalchemy
```

3. Run the data pipeline script to create the database

4. Open the Power BI report to explore dashboards

---

## 📈 Business Value

This project demonstrates a full analytics lifecycle — from automated data engineering to executive-level dashboards — helping organizations:

* Optimize pricing strategies
* Improve vendor selection
* Reduce margin risk
* Strengthen overall business performance

---

## 👤 Author

**Somnath Mondal**
Retail Operations & Vendor Performance Analytics

---

## ⭐ If you like this project

Consider giving the repository a star — it helps others discover the work!
