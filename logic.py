from gevent import monkey
monkey.patch_all()
from imageInfo import ImageInfo
from requests.packages.urllib3.util.ssl_ import create_urllib3_context
import grequests
from UrlParser import UrlParser


class Worker:
    def __init__(self, url):
        
        try:
            self.url = url
            create_urllib3_context()
            self.parser = UrlParser(self.url)
            self.response_arr = [grequests.get(url) for url in self.parser.urls]
            self.res = []
        except Exception as E:
            raise E

    def __set_result(self, **kwargs):
        self.res.append(dict(kwargs))

    def get_list(self):
        for req in grequests.map(self.response_arr, size=16, exception_handler=self.request_fail):
            obj = ImageInfo(req).image_size()
            obj.update({"url": req.url})
            self.__set_result(**obj)
        return self.res

    def request_fail(self, req, exception):
        return {"error": "request falling"}
