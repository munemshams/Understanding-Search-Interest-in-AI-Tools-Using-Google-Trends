import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------
# Load and prepare data
# -------------------------------------
df = pd.read_csv("ai_tools_comparison.csv")

df["week"] = pd.to_datetime(df["week"])
df = df.set_index("week")

# -------------------------------------
# 1. Most consistent growth
# -------------------------------------
growth = df.pct_change().fillna(0) * 100
std_values = growth.std()
most_consistent_tool = std_values.idxmin()

with open("most_consistent_tool.txt", "w") as f:
    f.write(most_consistent_tool)

# -------------------------------------
# 2. Largest decline in ChatGPT interest
# -------------------------------------
gpt_changes = df["chatgpt"].diff()
dip_week = gpt_changes.idxmin()
gpt_dip = dip_week.strftime("%B %Y")

with open("gpt_dip.txt", "w") as f:
    f.write(gpt_dip)

# -------------------------------------
# 3. Month with highest average interest
# -------------------------------------
# Use "ME" for month-end frequency since "M" is deprecated
monthly = df.resample("ME").mean()
best_month = monthly.mean(axis=1).idxmax().strftime("%B")

with open("best_month.txt", "w") as f:
    f.write(best_month)

# -------------------------------------
# 4. Visualization: Trend Plot
# -------------------------------------
plt.figure(figsize=(12, 6))
df.plot()
plt.title("Interest Levels Over Time (Google Trends)")
plt.xlabel("Week")
plt.ylabel("Interest Level")
plt.tight_layout()
plt.savefig("trend_plot.png")
plt.close()

# -------------------------------------
# 5. Visualization: Monthly Seasonality
# -------------------------------------
plt.figure(figsize=(10, 6))
monthly.plot(kind="line")
plt.title("Monthly Average Search Interest")
plt.xlabel("Month")
plt.ylabel("Average Interest Level")
plt.tight_layout()
plt.savefig("monthly_seasonality.png")
plt.close()

# -------------------------------------
# Optional: Console Outputs
# -------------------------------------
print("\nResults Generated:")
print("Most consistent tool:", most_consistent_tool)
print("ChatGPT largest decline:", gpt_dip)
print("Month with highest average interest:", best_month)
print("\nFiles created:")
print("- most_consistent_tool.txt")
print("- gpt_dip.txt")
print("- best_month.txt")
print("- trend_plot.png")
print("- monthly_seasonality.png")
