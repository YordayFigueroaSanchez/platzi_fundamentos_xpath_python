import requests
import lxml.html as html
from pprint import pprint

XPATH_TEST = '//a[class="keychainify-checked"]/text()'
XPATH_TEST2 = '//a/text()'
XPATH_TEST3 = '//a[@class]/text()'

HOME_URL = 'https://erikberg.com/mlb/scores/2022-04-14'

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            pprint(parsed)
            list_row = parsed.xpath(XPATH_TEST3)
            pprint(list_row)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)
def run():
    parse_home()


if __name__ == '__main__':
    run()