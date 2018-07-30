#!/usr/bin/env python
# coding=utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://youku.com/")
bs_obj = BeautifulSoup(html, features="html.parser")
print(bs_obj.a)
