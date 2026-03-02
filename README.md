**Understanding Search Interest in AI Tools Using Google Trends**

This project analyzes global search interest for three leading AI tools:

- ChatGPT

- Gemini

- Microsoft Copilot

Using weekly Google Trends data (past 12 months as of September 2024), the script uncovers:

- Which AI tool shows the most consistent growth

- When ChatGPT experienced its largest decline

- Which month had the highest average interest

- Visual patterns and seasonality trends

- Automatically generated output files and visualizations

This project provides actionable intelligence for understanding user interest dynamics across the AI landscape.

**Key Insights Generated**

1. Most consistent growth

Computed using week-over-week volatility across all tools.

2. ChatGPT’s largest decline

Detected using direction and magnitude of week-to-week drops.

3. Highest average interest month

Calculated using monthly aggregated averages across all tools.

All resulting values are saved into .txt files for easy referencing.

**Visualizations**

Two visualizations are automatically generated when running the script:

1. Trend Plot

Shows weekly interest for ChatGPT, Gemini, and Microsoft Copilot.

2. Monthly Seasonality

Shows the monthly average interest levels, useful for spotting seasonal patterns.

These images are saved directly to your project folder.

## 📁 Files Included

| File Name | Description |
|----------|-------------|
| `ai_trends_analysis.py` | Main Python script performing all analysis and generating outputs. |
| `ai_tools_comparison.csv` | Google Trends dataset for ChatGPT, Gemini, and Microsoft Copilot. |
| `most_consistent_tool.txt` | Tool with the most stable week-over-week growth. |
| `gpt_dip.txt` | Month & year of ChatGPT’s largest decline in search interest. |
| `best_month.txt` | Month with the highest overall average interest. |
| `trend_plot.png` | Visualization of weekly search interest levels. |
| `monthly_seasonality.png` | Visualization of monthly average search interest. |
| `README.md` | Full project documentation. |

