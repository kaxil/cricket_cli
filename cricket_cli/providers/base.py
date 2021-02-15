from bs4 import BeautifulSoup
import requests


class BaseProvider:
    def __init__(self, url: str):
        self.url = url

    @property
    def scrape_url(self):
        r = requests.get(self.url)
        page = BeautifulSoup(r.content, "html.parser")
        return page

    def livescore(self):
        raise NotImplementedError

    def commentary(self):
        raise NotImplementedError

    def scorecard(self):
        raise NotImplementedError
