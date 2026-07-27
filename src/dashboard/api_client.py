import requests

BASE_URL = "http://127.0.0.1:8000/api/v1"


def get_companies():
    return requests.get(f"{BASE_URL}/companies").json()


def get_company(ticker):
    return requests.get(
        f"{BASE_URL}/companies/{ticker}"
    ).json()


def get_screener(
    min_roe=0,
    min_opm=0
):
    return requests.get(
        f"{BASE_URL}/screener",
        params={
            "min_roe": min_roe,
            "min_opm": min_opm
        }
    ).json()


def get_sectors():
    return requests.get(
        f"{BASE_URL}/sectors"
    ).json()