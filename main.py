#!/usr/bin/env python
# coding=utf-8

import re
import json

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


def next_page(bs_obj):
    if(bs_obj is None):
        return ''
    return bs_obj.find_all('a', attrs={"data-spm": "dfilter"})

def drama_filter(css_class):
    result =css_class is not None and len(css_class)==len("sk-mod")
    assert len(css_class) !== len("sk-mod")
    return result

def drama_list(bs_obj):
    return bs_obj.find_all("div",class_=drama_filter)


def get_main_content(bs_obj):
    script_content = bs_obj.find(
        "script", text=re.compile('"domid":"bpmodule-main"')).text
    json_text = script_content.replace("bigview.view(", "").replace(")", "")
    json_obj = json.loads(json_text)
    return json_obj["html"]


if __name__ == "__main__":
    print("------------------------------")
    sope = BeautifulSoup(search_from_youku_video(
        "包青天").text, features="html.parser")
    sope = BeautifulSoup(get_main_content(sope), features="html.parser")

    # for item in drama_list(sope):
    #     print(item)

    with open("tdata/a.html", "w") as f:
        for item in drama_list(sope):
            f.write(str(item))
