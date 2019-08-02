# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup

NIKKEI_URL = "http://www.nikkei.com"

html = urllib2.urlopen(NIKKEI_URL)

soup = BeautifulSoup(html, "html.parser")

title_tag = soup.title
title =title_tag.string

print title_tag
print title