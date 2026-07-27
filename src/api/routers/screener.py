from fastapi import APIRouter
import sqlite3
import pandas as pd
import numpy as np

router = APIRouter()

DATABASE = "database/nifty100.db"


@router.get("/screener")
def screener(
    min_roe: float = 0,
    min_opm: float = 0
):

    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql(
        "SELECT * FROM analysis",
        conn
    )

    conn.close()

    # -----------------------------
    # Fix Headers
    # -----------------------------
    df.columns = df.iloc[0]
    df = df.iloc[1:].reset_index(drop=True)

    # -----------------------------
    # ROE
    # -----------------------------
    if "roe" in df.columns:

        df["roe"] = (
            df["roe"]
            .astype(str)
            .str.extract(r"(-?\d+\.?\d*)")[0]
        )

        df["roe"] = pd.to_numeric(
            df["roe"],
            errors="coerce"
        ).fillna(0)

    else:
        df["roe"] = 0

    # -----------------------------
    # OPM
    # -----------------------------
    if "opm_percentage" in df.columns:

        df["opm_percentage"] = pd.to_numeric(
            df["opm_percentage"],
            errors="coerce"
        ).fillna(0)

    else:
        df["opm_percentage"] = 0

    # -----------------------------
    # Filters
    # -----------------------------
    df = df[
        (df["roe"] >= min_roe) &
        (df["opm_percentage"] >= min_opm)
    ]

    # -----------------------------
    # Remove NaN for JSON
    # -----------------------------
    df = (
        df.replace([np.inf, -np.inf], np.nan)
          .where(pd.notnull(df), None)
    )

    return df.to_dict(orient="records")