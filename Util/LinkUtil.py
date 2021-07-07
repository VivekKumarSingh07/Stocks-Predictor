import requests
from bs4 import BeautifulSoup
from Constants.Urls import ECONOMIC_TIMES_RECOS_URL


def economic_times_links():
    return get_recos_links_from_economic_times()


def get_recos_links_from_economic_times():
    # List to store all the links in the website
    recos_links = []

    # making requests instance
    request_instance = requests.get(ECONOMIC_TIMES_RECOS_URL)

    # Using the BeautifulSoup module
    soup = BeautifulSoup(request_instance.text, 'html.parser')

    # Getting the links of the articles
    for anchors in soup.find_all('a'):
        anchor_text = anchors.get_text()
        anchor_links = anchors.get('href')
        if "Buy" in anchor_text and "/markets/stocks/recos/buy" in anchor_links:
            recos_links.append(anchor_links)

    return format_links_of_economic_times(recos_links)


# Updating the link to the correct format
def format_links_of_economic_times(recos_links):
    modified_recos_links = []
    for link in recos_links:
        index = link.rfind('/buy')
        new_link = ECONOMIC_TIMES_RECOS_URL + link[index:]

        # Removing the original link from the list
        # recos_links.remove(link)

        # Appending the new link to the list
        modified_recos_links.append(new_link)

    return modified_recos_links
