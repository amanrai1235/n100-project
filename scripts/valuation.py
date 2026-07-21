import os
import sqlite3
import pandas as pd

# -----------------------------
# Create Reports Folder
# -----------------------------
os.makedirs("reports", exist_ok=True)

# -----------------------------
# Connect Database
# -----------------------------
conn = sqlite3.connect("database/nifty100.db")

# -----------------------------
# Load Tables
# -----------------------------
analysis = pd.read_sql("SELECT * FROM analysis", conn)
profit = pd.read_sql("SELECT * FROM profitandloss", conn)

# -----------------------------
# Fix Headers
# -----------------------------
analysis.columns = analysis.iloc[0]
analysis = analysis.iloc[1:].reset_index(drop=True)

profit.columns = profit.iloc[0]
profit = profit.iloc[1:].reset_index(drop=True)

# -----------------------------
# Keep Required Columns
# -----------------------------
analysis = analysis[["company_id", "roe"]]

# -----------------------------
# Merge Tables
# -----------------------------
valuation = profit.merge(
    analysis,
    on="company_id",
    how="left"
)

# -----------------------------
# Clean ROE
# -----------------------------
valuation["roe"] = (
    valuation["roe"]
    .astype(str)
    .str.extract(r'(-?\d+\.?\d*)')[0]
)

valuation["roe"] = pd.to_numeric(
    valuation["roe"],
    errors="coerce"
)

# -----------------------------
# Convert Numeric Columns
# -----------------------------
numeric_cols = [
    "opm_percentage",
    "net_profit",
    "profit_before_tax",
    "eps"
]

for col in numeric_cols:
    valuation[col] = pd.to_numeric(
        valuation[col],
        errors="coerce"
    )

valuation = valuation.fillna(0)

# -----------------------------
# Create Valuation Score
# -----------------------------
valuation["valuation_score"] = (
    valuation["roe"] * 0.40
    + valuation["opm_percentage"] * 0.30
    + valuation["net_profit"] * 0.30
)

# -----------------------------
# Rating Function
# -----------------------------
def rating(score):
    if score >= 100:
        return "Strong"

    elif score >= 50:
        return "Moderate"

    else:
        return "Weak"


valuation["valuation_rating"] = valuation["valuation_score"].apply(rating)

# -----------------------------
# Final Report
# -----------------------------
final = valuation[
    [
        "company_id",
        "roe",
        "opm_percentage",
        "net_profit",
        "eps",
        "profit_before_tax",
        "valuation_score",
        "valuation_rating"
    ]
]

# -----------------------------
# Save Reports
# -----------------------------
csv_path = os.path.join("reports", "valuation_flags.csv")
excel_path = os.path.join("reports", "valuation_summary.xlsx")

final.to_csv(csv_path, index=False)
final.to_excel(excel_path, index=False)

# -----------------------------
# Console Output
# -----------------------------
print("=" * 60)
print("DAY 26 - VALUATION ANALYSIS COMPLETED")
print("=" * 60)

print("\nTotal Companies :", len(final))
print("\nValuation Summary")

print(
    final["valuation_rating"]
    .value_counts()
)

print("\nReports Generated Successfully")

print(csv_path)
print(excel_path)

conn.close()