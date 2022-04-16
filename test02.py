# lxml_parse.py

from lxml import etree
import requests

XPATH_TEST = '//div[@class="nba-stat-table__overflow"]/table/tbody/tr/td[@class="player-name first"]'
XPATH_TEST2 = '//div/table/tbody/tr/td[@class="player-name first"]/text()'
XPATH_TEST3 = '//div/table/tbody'

HOME_URL = 'https://www.nba.com/stats/players/boxscores/?Season=2021-22&SeasonType=Regular%20Season&DateFrom=04%2F04%2F2022&DateTo=04%2F05%2F2022'


response = requests.get(HOME_URL)
home = response.content.decode('utf-8')
html = etree.parse(home)
result = etree.tostring(html, pretty_print=True)

print(result)
