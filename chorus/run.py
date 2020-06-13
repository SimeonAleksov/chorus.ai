from .scraper import Scrape
import requests
from .config import *
from .serializer import serialize, save_json


def run():
    data = []
    scrape = Scrape(requests.session(), HEADERS)
    for i in range(1, 3):
        scrape.get(URL.format(page_num=i))
        scrape.make_soup()
        for obj in scrape.find_customers():
            scrape.get(obj)
            scrape.make_soup()
            for item in zip(scrape.get_company_name(), scrape.get_company_url(), scrape.get_company_logo()):
                data.append(serialize(item))
        save_json(data)
