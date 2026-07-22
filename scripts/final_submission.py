import os
import pandas as pd

print("=" * 60)
print("FINAL PROJECT SUBMISSION")
print("=" * 60)

reports = [
    "reports/valuation_flags.csv",
    "reports/valuation_summary.xlsx",
    "reports/qa_summary.csv",
    "reports/final_submission_report.csv"
]

summary = []

for report in reports:

    available = os.path.exists(report)

    summary.append({
        "Report": report,
        "Status": "Available" if available else "Missing"
    })

summary = pd.DataFrame(summary)

print(summary)

summary.to_csv(
    "reports/final_submission_report.csv",
    index=False
)

print("\nProject Ready For Submission.")