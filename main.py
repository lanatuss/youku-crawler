#!/usr/bin/env python
# coding=utf-8

# from urllib.request import urlopen
# from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
from requests.compat import urljoin, urlencode


START_URL = "http://www.soku.com/search_video/"


def createSearchURL(key, prefix='q_'):
    key = prefix + urlencode(key)
    return urljoin(START_URL, key)
