#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup

import requests
from requests.compat import urljoin, urlencode

START_URL = "http://www.soku.com/search_video/"

def createSearchURL(key, prefix='q_'):
    key = prefix + key
    return urljoin(START_URL, key)

def search_from_youku_video(key):
    url = createSearchURL(key)
    r = requests.get(url)
    return r

if __name__ == "__main__":
    bs_obj = BeautifulSoup(search_from_youku_video("包青天"))
