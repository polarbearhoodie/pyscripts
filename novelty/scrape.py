import os
import time
import requests
from bs4 import BeautifulSoup as BSoup

def scrape(base_url, search_word="Volume"):
    page = requests.get(base_url)
    page_parse = BSoup(page.content, "html.parser")

    # title = str(page_parse.title.getText()).split()[:2] # two words
    # title_name = "{} {}".format(title[0], title[1])

    links = [link.get('href') for link in page_parse.find_all('a') if search_word in link.getText()]
    links = [requests.get(link).url for link in links]

    return links


def invoke_multi_scrape(filename="url_data.txt"):
    file = open(filename, "r")
    multi_links = []
    for line in file:
        multi_links.extend(scrape(line))

    return multi_links


def follow_links(links):
    for url in links:
        os.system("start msedge " + url)
        time.sleep(2)

all_links = invoke_multi_scrape()
follow_links(all_links)


