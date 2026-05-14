# 🍳 Cloud Kitchen P&L Intelligence Dashboard

> AI-Powered Financial & Operational Analytics System for Cloud Kitchens

---

## 📌 Overview

The **Cloud Kitchen P&L Intelligence Dashboard** is an advanced business analytics solution designed to analyze the financial and operational performance of cloud kitchens across multiple stores, cities, and operational zones.

This project transforms raw kitchen-level P&L data into actionable business insights through interactive dashboards, KPI tracking, variance intelligence, and profitability analytics.

The solution helps business stakeholders:

- Monitor operational efficiency
- Track EBITDA and contribution margins
- Detect inventory and operational leakages
- Analyze city-wise and store-wise performance
- Identify profitable and loss-making kitchens
- Make data-driven strategic decisions

---

# 🚀 Key Features

## 🏪 Kitchen Level P&L Dashboard

- Revenue Tracking
- Gross Margin Analysis
- EBITDA Monitoring
- Store-wise Performance Analysis
- City-wise Comparison
- Profitability Distribution
- Revenue vs EBITDA Analysis
- Top & Bottom Performing Kitchens
- Interactive KPI Cards
- Multi-level Filtering System

---

## 📉 Variance Intelligence Dashboard

- Variance Distribution Analysis
- Revenue Bucket Segmentation
- Variance Bucket Monitoring
- Operational Leakage Detection
- Variance vs Revenue Mapping
- City-wise Variance Tracking
- Heatmaps & Trend Analysis
- High-risk Store Identification

---

# 📊 Business Problem

Cloud kitchen businesses operate with:

- Thin operational margins
- High inventory sensitivity
- Dynamic demand fluctuations
- Operational inefficiencies
- Wastage and leakage risks

Traditional reporting systems often fail to provide real-time visibility into profitability and operational performance.

This project solves that challenge by building a centralized analytics platform capable of monitoring financial health and operational efficiency across all kitchen locations.

---

# 🧠 Objectives

The primary objectives of this project were:

- Analyze kitchen profitability
- Monitor revenue and EBITDA trends
- Detect operational inefficiencies
- Identify high variance kitchens
- Segment stores into business cohorts
- Compare performance across cities
- Enable executive-level decision making
- Build a scalable analytics dashboard

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Plotly | Interactive Visualizations |
| Streamlit | Dashboard Development |
| OpenPyXL | Excel File Processing |
| Matplotlib | Exploratory Analysis |
| Seaborn | Correlation Analysis |

---

# 📂 Dataset Information

The dataset contains operational and financial records of cloud kitchens.

## Important Columns

| Column | Description |
|---|---|
| MONTH | Reporting Month |
| STORE | Kitchen Identifier |
| CITY | Store Location |
| ZONE MAPPING | Operational Zone |
| STATUS | Active/Inactive Status |
| NET REVENUE | Revenue Generated |
| GROSS MARGIN | Contribution Margin |
| KITCHEN EBITDA | Operational Profitability |
| VARIANCE | Operational Variance |
| REVENUE COHORT | Revenue Category |
| EBITDA CATEGORY | Profitability Category |

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Missing value handling
- Duplicate removal
- Data type corrections
- KPI engineering
- Percentage calculations
- Revenue segmentation
- Variance bucket creation
- EBITDA categorization

---

# 🏗️ Feature Engineering

## Gross Margin %

```python
df["GM%"] = (
    df["GROSS MARGIN"] /
    df["NET REVENUE"]
) * 100
```

Measures contribution margin efficiency.

---

## EBITDA %

```python
df["EBITDA%"] = (
    df["KITCHEN EBITDA"] /
    df["NET REVENUE"]
) * 100
```

Measures operational profitability.

---

## Variance %

```python
df["VARIANCE%"] = (
    df["VARIANCE"] /
    df["NET REVENUE"]
) * 100
```

Tracks operational leakages and inefficiencies.

---

# 📈 Exploratory Data Analysis

The project includes extensive exploratory analysis such as:

- Monthly Revenue Trends
- EBITDA Trend Analysis
- City-wise Performance Analysis
- Revenue Distribution
- Profitability Segmentation
- Variance Distribution
- Revenue Cohort Analysis
- Store Benchmarking
- Correlation Analysis

---

# 🔍 Key Insights

## Revenue Insights

- Revenue concentration was observed among selected high-performing kitchens.
- Seasonal fluctuations impacted monthly revenue trends.
- Certain cities consistently outperformed others.

---

## EBITDA Insights

- Several stores generated strong revenue but weak EBITDA.
- Indicates operational inefficiencies and poor cost management.

---

## Variance Insights

High variance kitchens may indicate:

- Inventory leakage
- Food wastage
- Procurement inefficiencies
- Demand forecasting errors
- Operational mismanagement

---

## Profitability Insights

- Multiple kitchens remained consistently profitable.
- Certain stores showed persistent negative EBITDA.

---

# 📊 Dashboard Highlights

## Executive KPI Cards

- Total Revenue
- Gross Margin
- EBITDA
- Store Count
- Profitability %

---

## Interactive Analytics

- Multi-tab Dashboards
- Dynamic Filters
- Scatterplots
- Heatmaps
- Revenue Trends
- Variance Trends
- Cohort Analysis

---

# 🎯 Strategic Recommendations

Based on analysis:

- Reduce operational leakages in high variance kitchens
- Improve inventory forecasting
- Optimize procurement systems
- Focus expansion on high-margin cities
- Monitor persistently loss-making kitchens
- Improve operational efficiency

---

# 📁 Project Structure

```bash
Cloud-Kitchen-PNL-Dashboard/
│
├── app.py
├── Kittchen PNL Data.xlsx
├── requirements.txt
├── README.md
└── notebooks/
    └── analysis.ipynb
```

---

# ▶️ Running the Project

## 1️⃣ Clone Repository

```bash
git clone <repository-url>
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

# 📦 Requirements

```txt
streamlit
pandas
numpy
plotly
openpyxl
matplotlib
seaborn
```

---

# 🔮 Future Improvements

Potential enhancements include:

- Machine Learning Forecasting
- Demand Prediction Models
- Inventory Optimization
- SQL Database Integration
- Automated Alert Systems
- AI-powered Recommendations
- Real-time Data Pipelines

---

# 📚 Skills Demonstrated

- Financial Analytics
- Business Intelligence
- KPI Engineering
- Dashboard Development
- Data Visualization
- Data Storytelling
- Operational Analytics
- Executive Reporting

---

# 🏆 Conclusion

The **Cloud Kitchen P&L Intelligence Dashboard** successfully transformed raw operational data into a scalable analytics platform capable of delivering actionable business intelligence.

The project demonstrates:

- Strong analytical thinking
- Financial understanding
- Operational intelligence
- Advanced dashboard engineering
- Business-oriented problem solving

---

# 👨‍💻 Author

## Shivam Shukla

Aspiring Data Scientist | Analytics Engineer | Business Intelligence Enthusiast

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
