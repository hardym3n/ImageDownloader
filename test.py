import requests
from bs4 import BeautifulSoup
import re


__scan_result = requests.get("https://forum.awd.ru/viewtopic.php?f=1011&t=165935")
__DOM = BeautifulSoup(__scan_result.text, "html.parser")
print(__DOM.find_all("img"))