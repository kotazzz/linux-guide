import logging
import yaml
import re
from itertools import groupby
import collections
from git import Repo
from datetime import datetime

#logging.basicConfig(filename="latest.log", encoding="utf-8", level=logging.DEBUG)
rawl = open("data.yml").read()
yaml = yaml.safe_load(rawl)


class DataReHandler:
    n = 0

    def __init__(self, res):
        def handler(element):
            print(f"{self.n} run")
            self.n += 1
            exec("def html_res():\n" + element[5:-3], globals())
            return str(html_res())

        self.res = list(map(handler, res))

    def __call__(self):
        return self.res.pop(0)


html = open("input.html").read()
finded_res = re.findall(r"<!--!.+?-->", html, re.DOTALL)
data_handler = DataReHandler(finded_res)
while True:
    if data_handler.res != []:
        html = re.sub(r"<!--!.+?-->", data_handler(), html, 1, flags=re.DOTALL)
    else:
        break

with open("index.html", "w", encoding="utf-8") as output_file:
    output_file.write(html)
