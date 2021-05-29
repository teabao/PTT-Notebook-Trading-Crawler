import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup


def get_data(i, page_idx, test_num, titles, prices, locations):

    print('\ri = {}\t page_idx = {}\t Loading...  {:.2f}%\t{}'.format(i, page_idx, (i/test_num)*100, datetime.now()), end='')

    res = requests.get(f'https://www.ptt.cc/bbs/nb-shopping/index{page_idx}.html')
    soup = BeautifulSoup(res.text, "lxml")

    for a in soup.select('.title a')[::-1]:

        if not a.string:
            continue
        title_search = re.search('賣/ *(?P<location>[^/]*)(.*)(〕|］|\])( *)(?P<content>.*)', a.string)

        try:
            location = title_search.group('location')
            title = title_search.group('content')
        except AttributeError:
            continue

        res_article = requests.get(f'https://www.ptt.cc{a["href"]}')
        soup_article = BeautifulSoup(res_article.text, "lxml")

        content = soup_article.find('div', id='main-content')
        if content:
            price_line = re.search('((價格)|(金額)|(价格))(.*)\n', content.text)
            if price_line:
                price = re.search('\d+', price_line.group().replace(',', ''))
                if price:
                    titles.append(title.upper())
                    prices.append(int(price.group()))
                    locations.append(str(location).strip())
