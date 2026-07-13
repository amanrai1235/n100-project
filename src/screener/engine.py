def filter_companies(
    data,
    roe_min=None,
    debt_to_equity_max=None,
    interest_coverage_min=None,
    asset_turnover_min=None,
    dividend_payout_min=None
):
    result = data.copy()

    if roe_min is not None:
        result = result[
            result["return_on_equity_pct"] >= roe_min
        ]

    if debt_to_equity_max is not None:
        result = result[
            result["debt_to_equity"] <= debt_to_equity_max
        ]

    if interest_coverage_min is not None:
        result = result[
            result["interest_coverage"] >= interest_coverage_min
        ]

    if asset_turnover_min is not None:
        result = result[
            result["asset_turnover"] >= asset_turnover_min
        ]

    if dividend_payout_min is not None:
        result = result[
            result["dividend_payout_ratio"] >= dividend_payout_min
        ]

    return result