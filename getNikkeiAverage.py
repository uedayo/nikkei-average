# config: UTF-8
import urllib2
from bs4 import BeautifulSoup

STOCK_URL = "http://www.nikkei.com/markets/kabu/"
TARGET_CLASS = "mkc-stock_prices"

html = urllib2.urlopen(STOCK_URL)

soup = BeautifulSoup(html, "html.parser")

# pick all span elements
span = soup.find_all("span")

# initialize to avoid print error
nikkei_average = ""

# find span element which has TARGET_CLASS out from every span elements
for tag in span:
    try:
        string_ = tag.get("class").pop(0)

        if string_ in TARGET_CLASS:
            nikkei_average = tag.string
            break
    except:
        pass

print nikkei_average