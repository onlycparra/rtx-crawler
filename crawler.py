#!/usr/bin/env python3
import sys
import re
import os
import requests
import statistics as stats
import urllib3
urllib3.disable_warnings()
from bs4 import BeautifulSoup as Soup

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

if __name__ == "__main__":
    url = "https://orangecounty.craigslist.org/search/sss?query=RTX+3080+Ti&sort=rel&srchType=T"
    html = requests.get(url, verify=False).content
    doc = Soup(html, 'html.parser')

    prices = doc.select('.result-meta > .result-price')
    prices = sorted([int(re.sub(r'[$,]','', x.text)) for x in prices])
    pr1 = prices.copy()
    pr2 = prices.copy()
    sample = len(prices)
    avg = stats.mean(prices)
    std = stats.stdev(prices)
    outliers = 0
    i = 0
    f = 1.1
    while i<sample:
        if prices[i] < (avg - f*std) or prices[i] > (avg + f*std):
            del prices[i]
            pr2[i+outliers] = "-"
            outliers += 1
            if i + outliers == sample:
                break
        else:
            i += 1

    min_ = min(prices)
    avg = stats.mean(prices)
    max_ = max(prices)
    eprint(f'search : {url}\n'\
           f'results: {sample}\n'\
           f'extreme: {outliers} (+-{f}*std)\n'\
           f'minimum: {min_:.2f}\n'\
           f'average: {round(avg,2)}\n'\
           f'maximum: {max_:.2f}\n'\
           f'std dev: {round(std,2)}')

    print(f'{sample},{outliers},{min_},{avg},{max_},{std}')
    # for a,b in zip(pr1, pr2):
    #     print(f'{a}\t{b}')
