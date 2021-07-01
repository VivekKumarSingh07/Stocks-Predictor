from Util.DataExtractionUtil import extract_companies_from_indices


def moving_average_algorithm_impl(market_index, time_period, stock_exchange="NSE"):
    print(extract_companies_from_indices(market_index))


moving_average_algorithm_impl("ind_nifty50list", 0)
