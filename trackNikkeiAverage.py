# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
import csv

STOCK_URL = "http://www.nikkei.com/markets/kabu/"
TARGET_CLASS = "mkc-stock_prices"
CSV_FILE_NAME = 'nikkei_heikin.csv'

html = urllib2.urlopen(STOCK_URL)

soup = BeautifulSoup(html, "html.parser")

# pick all span elements
span = soup.find_all("span")

# initialize to avoid print error
nikkei_average = ""

# 
f = open(CSV_FILE_NAME, 'a')
writer = csv.writer(f, lineterminator='\n')

csv_list = []
time_ = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
csv_list.append(time_)

# find span element which has TARGET_CLASS out from every span elements
for tag in span:
    try:
        string_ = tag.get("class").pop(0)

        if string_ in TARGET_CLASS:
            nikkei_average = tag.string
            break
    except:
        pass

csv_list.append(nikkei_average)

writer.writerow(csv_list)

f.close()
