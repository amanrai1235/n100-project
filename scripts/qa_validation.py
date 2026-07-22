import os
import sqlite3
import pandas as pd

print("=" * 60)
print("DAY 27 - QUALITY ASSURANCE")
print("=" * 60)

# -------------------------------------------------------
# Create reports folder if not exists
# -------------------------------------------------------
os.makedirs("reports", exist_ok=True)

# -------------------------------------------------------
# Connect Database
# -------------------------------------------------------
db_path = "database/nifty100.db"

if not os.path.exists(db_path):
    db_path = "./database/nifty100.db"

conn = sqlite3.connect(db_path)

# -------------------------------------------------------
# Check Available Tables
# -------------------------------------------------------
tables = pd.read_sql("""
SELECT name
FROM sqlite_master
WHERE type='table';
""", conn)

print("\nAvailable Tables")
print(tables)

# -------------------------------------------------------
# Record Count Validation
# -------------------------------------------------------
summary = []

print("\nTable Record Counts\n")

for table in tables["name"]:

    try:

        df = pd.read_sql(f"SELECT * FROM {table}", conn)

        rows = len(df)
        cols = len(df.columns)
        missing = df.isnull().sum().sum()
        duplicate = df.duplicated().sum()

        summary.append({
            "table": table,
            "rows": rows,
            "columns": cols,
            "missing_values": missing,
            "duplicate_rows": duplicate,
            "status": "PASS"
        })

        print(f"{table:20} Rows={rows}")

    except Exception as e:

        summary.append({
            "table": table,
            "rows": 0,
            "columns": 0,
            "missing_values": 0,
            "duplicate_rows": 0,
            "status": "FAIL"
        })

        print(f"{table} -> ERROR")

# -------------------------------------------------------
# Save QA Summary
# -------------------------------------------------------
qa_summary = pd.DataFrame(summary)

csv_path = "reports/qa_summary.csv"

if not os.path.exists("reports"):
    os.makedirs("reports")

qa_summary.to_csv(csv_path, index=False)

print("\nQA Summary Saved")

# -------------------------------------------------------
# Check Reports
# -------------------------------------------------------
print("\nReport Validation")

files = [
    "reports/valuation_flags.csv",
    "reports/valuation_summary.xlsx",
    "reports/qa_summary.csv"
]

for file in files:

    if os.path.exists(file):
        print("PASS :", file)
    else:
        print("MISSING :", file)

# -------------------------------------------------------
# Final Summary
# -------------------------------------------------------
print("\nOverall QA Result")

print(qa_summary)

conn.close()

print("\nQA Completed Successfully.")