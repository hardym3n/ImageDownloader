import requests
from bs4 import BeautifulSoup
import re


class UrlParser:
    def __init__(self, url):
        self.url = url
        self.__scan_result = requests.get(self.url)
        self.__DOM = BeautifulSoup(self.__scan_result.text, "html.parser")
        self.__domain = re.findall(r"^(?:\/\/|[^\/]+)*", self.url)[0]
        self.urls = []
        self.url_list()
        self.normalize_src()
        print("NON FORMATED URLS", self.urls)

    def image_list(self):
        return self.__DOM.find_all("img")

    def url_list(self):
        image_list = self.image_list()
        self.urls = []
        for item in image_list:
            if item.get('src'):
                self.urls.append(item['src'])
            elif item.get('data-src'):
                self.urls.append(item['data-src'])

    def normalize_src(self):
        for i, src_link in enumerate(self.urls):
            if src_link[0] != 'h':
                self.urls[i] = re.sub(r'(^\W+)', f'{self.__domain}/', src_link)