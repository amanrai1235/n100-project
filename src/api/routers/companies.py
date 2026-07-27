from fastapi import APIRouter, HTTPException
import sqlite3
import pandas as pd

router = APIRouter()

DATABASE = "database/nifty100.db"


@router.get("/companies")
def get_companies():
    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql("SELECT * FROM companies", conn)

    conn.close()

    df = df.fillna("")

    return df.to_dict(orient="records")


@router.get("/companies/{ticker}")
def get_company(ticker: str):

    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql(
        "SELECT * FROM companies",
        conn
    )

    conn.close()

    df = df.fillna("")

    # Second column me ticker hai (ABB, TCS, etc.)
    result = df[
        df.iloc[:,1].astype(str).str.upper() == ticker.upper()
    ]

    if result.empty:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    return result.to_dict(orient="records")[0]