from gevent import monkey
monkey.patch_all()

from UrlParser import UrlParser
import grequests
from requests.packages.urllib3.util.ssl_ import create_urllib3_context
from imageInfo import ImageInfo


def request_fail(req, exception):
    print("Request Failed", req.url)

create_urllib3_context()
url2 = UrlParser("https://zastava-ermaka.ru/ru/news/post/reliktovyj-les")
info_urls = url2.urls
print(info_urls)

response_arr = [grequests.get(url) for url in info_urls]
print("REQUEST PASS")
print(response_arr)

res = []
for req in grequests.map(response_arr, size=16, exception_handler=request_fail):
    res.append(ImageInfo(req).image_size())

print(res)