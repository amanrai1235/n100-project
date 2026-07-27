from fastapi import APIRouter
from src.api.database import get_connection

router = APIRouter()

@router.get("/health")
def health():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    )

    tables = [row[0] for row in cursor.fetchall()]

    conn.close()

    return {
        "status": "ok",
        "database": "connected",
        "tables": len(tables),
        "table_names": tables
    }