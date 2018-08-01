#!/usr/bin/env python
# coding=utf-8

import re
import json

from bs4 import BeautifulSoup

import requests
from requests.compat import urljoin, urlencode


START_URL = "http://www.soku.com/search_video/"


class DramaInfo(object):
    """影视剧或者综艺、视频等"""

    def __init__(self, tag):
        super(DramaInfo, self).__init__()
        self.name = tag.find(class_="mod-header").h2.a["title"]
        self.play_page_url = tag.find(class_="mod-header").h2.a["href"]
        self.type = tag.find(class_="base-type").text
        self.publish_year = tag.find("span", class_="spc-lv-1")
        self.image_url = tag.find("img")["src"]

        tmp_tags = tag.find_all(class_="spc-lv-4")

        # TODO: 解析导演和主演的html
        for tmp_tag in tmp_tags:
            if(tmp_tag.label.text == "导演"):
                self.director = tmp_tag.find_all("a")
            elif(tmp_tag.label.text=="主演"):
                self.starring = tmp_tag.find_all("a")
        
        self.synopsis = tmp_tag.find(class_="row-ellipsis").span.string
        self.home_page_url = tmp_tag.find(class_="row-ellipsis").a["href"]


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


def drama_filter(tag):
    return tag.has_attr(
        "class") and len(tag["class"]) == 1 and tag["class"][0] == "sk-mod"


def drama_list(bs_obj):
    return bs_obj.find_all(drama_filter)


def parse_drama_info(tag):


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

    with open("tdata/a.html", "w") as f:
        for item in drama_list(sope):
            f.write(str(item))
