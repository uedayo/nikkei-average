# config: UTF-8
import urllib2
from bs4 import BeautifulSoup

STOCK_URL = "http://www.nikkei.com/markets/kabu/"

html = urllib2.urlopen(STOCK_URL)

soup = BeautifulSoup(html, "html.parser")

print soup.title.string
