from fastapi import APIRouter
import sqlite3
import pandas as pd
import numpy as np

router = APIRouter()

DATABASE = "database/nifty100.db"


@router.get("/sectors")
def get_sectors():

    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql(
        "SELECT * FROM companies",
        conn
    )

    conn.close()

    # Fix header
    df.columns = df.iloc[0]
    df = df.iloc[1:].reset_index(drop=True)

    # Since dataset has no sector column
    df["sector"] = "Unknown"

    summary = (
        df.groupby("sector")
        .size()
        .reset_index(name="company_count")
    )

    # Remove NaN / Inf
    summary = summary.replace([np.inf, -np.inf], np.nan)
    summary = summary.fillna("")

    # Convert numpy objects into Python objects
    records = []

    for row in summary.to_dict(orient="records"):

        clean = {}

        for key, value in row.items():

            if pd.isna(value):
                clean[key] = ""

            elif isinstance(value, np.integer):
                clean[key] = int(value)

            elif isinstance(value, np.floating):
                clean[key] = float(value)

            else:
                clean[key] = str(value)

        records.append(clean)

    return records


@router.get("/sectors/{sector}/companies")
def sector_companies(sector: str):

    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql(
        "SELECT * FROM companies",
        conn
    )

    conn.close()

    # Fix header
    df.columns = df.iloc[0]
    df = df.iloc[1:].reset_index(drop=True)

    # Since dataset has no sector column
    df["sector"] = "Unknown"

    result = df[
        df["sector"].str.lower() == sector.lower()
    ].copy()

    # Replace NaN / Inf
    result = result.replace([np.inf, -np.inf], np.nan)
    result = result.fillna("")

    # Convert numpy objects into Python objects
    records = []

    for row in result.to_dict(orient="records"):

        clean = {}

        for key, value in row.items():

            if pd.isna(value):
                clean[key] = ""

            elif isinstance(value, np.integer):
                clean[key] = int(value)

            elif isinstance(value, np.floating):
                clean[key] = float(value)

            else:
                clean[key] = str(value)

        records.append(clean)

    return records