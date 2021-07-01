"""Utility to download various charts/indices"""
import requests


# Downloads the company list and its detail with respect to market index
def download_companies_in_market_indices(market_index):
    market_index = market_index + ".csv"
    market_index_url = "https://www1.nseindia.com/content/indices/" + market_index
    req = requests.get(market_index_url)
    url_content = req.content
    # TODO 1 make this generic for all the OS. Currently its for windows
    csv_file = open("../Downloads/" + market_index, 'wb')
    csv_file.write(url_content)
    csv_file.close()
