from bs4 import BeautifulSoup
import requests.exceptions


class Scrape:
    def __init__(self, session, headers, proxy=None):
        self.session = session
        self.headers = headers
        self.proxy = proxy
        self.response = None
        self.soup = None

    def get(self, url):
        try:
            self.response = self.session.get(url, headers=self.headers, verify=False)
        except requests.exceptions.ConnectionError:
            print("Connection error, try again maybe.")

    def get_response(self):
        return self.response

    def make_soup(self):
        self.soup = BeautifulSoup(self.response.text, 'html.parser')

    def find_customers(self):
        try:
            for item in self.soup.find_all("div", {"class": "card-post__inner"}):
                url = item.a['href']
                yield url
        except AttributeError:
            print("Attribute name changed or something.")

    def get_company_name(self):
        try:
            company_name = self.soup.find_all("a", {"class": "breadcrumb__link"})
            for item in company_name:
                if item.text != "Case Study":
                    yield item.text
        except AttributeError:
            print("Attribute name changed or something.")

    def get_company_url(self):
        try:
            company_url = self.soup.find_all("span", {"class": "alt-btn__text"})
            for item in company_url:
                yield item.text
        except AttributeError:
            print("Attribute name changed or something.")

    def get_company_logo(self):
        try:
            company_logo = self.soup.find_all("div", {"class": "about-company__logo"})
            for item in company_logo:
                yield item.img['src']
        except AttributeError:
            print("Attribute name changed or something.")
