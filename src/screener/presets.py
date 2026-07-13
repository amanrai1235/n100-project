def quality_screener(data):
    return data[
        (data["return_on_equity_pct"] >= 15) &
        (data["debt_to_equity"] <= 1) &
        (data["interest_coverage"] >= 3)
    ].copy()


def low_debt_screener(data):
    return data[
        data["debt_to_equity"] <= 0.5
    ].copy()


def high_roe_screener(data):
    return data[
        data["return_on_equity_pct"] >= 20
    ].copy()


def income_screener(data):
    return data[
        (data["dividend_payout_ratio"] >= 20) &
        (data["return_on_equity_pct"] >= 10)
    ].copy()


def balanced_screener(data):
    return data[
        (data["return_on_equity_pct"] >= 12) &
        (data["debt_to_equity"] <= 1.5) &
        (data["asset_turnover"] >= 0.5)
    ].copy()