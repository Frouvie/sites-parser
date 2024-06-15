from requests import get
from bs4 import BeautifulSoup

def parse_sites(links):
    for link in links:
        responce = get(link)
        html = BeautifulSoup(responce.content, "xml")
        tags = html.find_all(["p", "h1", "h2", "h3"])

        return tags