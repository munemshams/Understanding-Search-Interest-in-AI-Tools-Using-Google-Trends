# Analyzing Search Interest in AI Tools Using Google Trends

Artificial Intelligence tools have rapidly become part of everyday workflows, influencing productivity, research, and software development. Understanding how public interest evolves over time can provide insights into adoption trends, competitive positioning, and technology awareness.

This project analyzes **Google Trends search interest data** for three major AI tools:

- ChatGPT  
- Google Gemini  
- Microsoft Copilot  

Using weekly Google Trends data collected over the past 12 months (as of September 2024), the project explores how search demand for these tools has evolved over time and identifies key patterns in user interest.

The analysis produces both **quantitative insights and visualizations** that highlight growth trends, seasonality, and shifts in public attention across the AI landscape.

---

# Project Overview

The goal of this project is to examine how search interest changes over time for leading AI platforms.

Using Python-based data analysis, the project investigates:

- Which AI tool shows the most consistent growth
- When ChatGPT experienced its largest decline in interest
- Which month recorded the highest overall search interest
- Whether seasonal patterns exist in AI search trends

The script processes weekly Google Trends data and automatically generates summary insights and visualizations.

---

# Dataset

The dataset used in this project contains **weekly Google Trends search interest values** for three AI tools:

- ChatGPT
- Gemini
- Microsoft Copilot

File included in the repository:

`ai_tools_comparison.csv`

Each record represents the relative search interest for a given week.

Google Trends values range from **0–100**, where:

- **100** represents the highest relative search interest during the selected time period
- Other values represent search interest relative to that peak

---

# Project Workflow

The analysis follows a structured **data analytics workflow**.

## 1. Data Loading

The Google Trends dataset is loaded using **pandas**.

Initial steps include:

- Inspecting the dataset
- Ensuring correct date formatting
- Preparing weekly trend values for analysis

---

## 2. Weekly Trend Analysis

The script evaluates **week-over-week changes in search interest** for each AI tool.

By measuring volatility in these changes, the analysis identifies the tool with the **most consistent growth pattern**.

The result is saved to:

`most_consistent_tool.txt`

---

## 3. ChatGPT Decline Detection

To identify the largest drop in interest for ChatGPT:

- Week-to-week differences are calculated
- The largest negative change is detected
- The corresponding week is identified

The result is saved to:

`gpt_dip.txt`

---

## 4. Monthly Aggregation

Weekly search values are aggregated into **monthly averages**.

This allows the project to determine which month had the **highest overall search interest across all tools**.

The result is saved to:

`best_month.txt`

---

## 5. Visualization

The project generates two visualizations to better understand trends in the dataset.

### Weekly Trend Plot

Displays weekly search interest for:

- ChatGPT
- Gemini
- Microsoft Copilot

Saved as:

`trend_plot.png`

---

### Monthly Seasonality Plot

Displays the **average search interest by month**, allowing seasonal patterns to be observed.

Saved as:

`monthly_seasonality.png`

---

# Files Included

| File | Description |
|-----|-------------|
| `ai_trends_analysis.py` | Main Python script performing the data analysis and generating outputs |
| `ai_tools_comparison.csv` | Google Trends dataset containing weekly search interest values |
| `most_consistent_tool.txt` | Identifies which AI tool shows the most consistent weekly growth |
| `gpt_dip.txt` | Records the week of ChatGPT’s largest decline in search interest |
| `best_month.txt` | Indicates the month with the highest average search interest |
| `trend_plot.png` | Visualization of weekly search interest trends |
| `monthly_seasonality.png` | Visualization of monthly average search interest |
| `README.md` | Project documentation |

---

# Python Libraries Used

The project was implemented using the following Python libraries:

- pandas
- matplotlib

---

# Key Outcomes

This project demonstrates how publicly available trend data can be used to analyze technology adoption patterns.

The analysis successfully:

- Identified the AI tool with the **most stable growth pattern**
- Detected the **largest week-over-week decline in ChatGPT search interest**
- Determined the **month with the highest average search demand**
- Generated visualizations to highlight trend patterns and seasonality

These insights provide a snapshot of how global interest in major AI tools has evolved over the past year.

---

# Technologies Used

Python  
Pandas  
NumPy  
Matplotlib  

---

# Author

**Munem Shariar Shams**

Data Analytics | Python | SQL | Data Visualization
