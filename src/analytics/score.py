import pandas as pd


def normalize_positive(series):
    min_value = series.min()
    max_value = series.max()

    if max_value == min_value:
        return pd.Series(
            50,
            index=series.index
        )

    return (
        (series - min_value) /
        (max_value - min_value)
    ) * 100


def normalize_negative(series):
    min_value = series.min()
    max_value = series.max()

    if max_value == min_value:
        return pd.Series(
            50,
            index=series.index
        )

    return (
        (max_value - series) /
        (max_value - min_value)
    ) * 100


def calculate_composite_score(data):
    result = data.copy()

    result["roe_score"] = normalize_positive(
        result["return_on_equity_pct"]
    )

    result["debt_score"] = normalize_negative(
        result["debt_to_equity"]
    )

    result["interest_score"] = normalize_positive(
        result["interest_coverage"]
    )

    result["asset_turnover_score"] = normalize_positive(
        result["asset_turnover"]
    )

    result["dividend_score"] = normalize_positive(
        result["dividend_payout_ratio"]
    )

    result["composite_score"] = (
        result["roe_score"] * 0.30
        + result["debt_score"] * 0.25
        + result["interest_score"] * 0.20
        + result["asset_turnover_score"] * 0.15
        + result["dividend_score"] * 0.10
    )

    return result