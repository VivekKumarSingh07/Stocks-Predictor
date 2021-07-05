"""Utility to extract meaningful data from various files"""
from Util.DownloadUtil import download_companies_in_market_indices
from csv import reader


# Extracts the company list which from market index
def extract_companies_from_indices(market_index):
    download_companies_in_market_indices(market_index)
    company_list = []
    with open('../Downloads/' + market_index + '.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            company_list.append(row[2])
    return company_list


# Extract data from the economic times links
def extract_info_from_et_links(links):
    print(links)
