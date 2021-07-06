"""Utility to extract meaningful data from various files"""
import re
from Util.DownloadUtil import download_companies_in_market_indices
import csv


# Extracts the company list which from market index
def extract_companies_from_indices(market_index):
    download_companies_in_market_indices(market_index)
    company_list = []
    with open('../Downloads/' + market_index + '.csv', 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            company_list.append(row[2])
    return company_list


# Extract data from the economic times links
def extract_info_from_et_links(links):
    with open("../Downloads/stocks_recommended_by_ET.csv", 'w', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # TODO 2 go to url and check if it is Intraday or Swing trading
        for link in links:
            stock = re.search('buy-(.+?)-target', link).group(1)
            target = re.search('rs-(.+?)-', link).group(1)
            reviewed_by = re.search('rs-[0-9]+-(.+?)/articleshow', link).group(1)
            row = [stock, target, reviewed_by]
            csvwriter.writerow(row)


