import requests
import lxml.html as html

XPATH_TEST = '//div[@class="nba-stat-table__overflow"]/table/tbody/tr/td[@class="player-name first"]'
XPATH_TEST2 = '//div/table/tbody/tr/td[@class="player-name first"]/text()'

HOME_URL = 'https://www.nba.com/stats/players/boxscores/?Season=2021-22&SeasonType=Regular%20Season&DateFrom=04%2F04%2F2022&DateTo=04%2F05%2F2022'

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            print(parsed)
            list_row = parsed.xpath(XPATH_TEST2)
            print(list_row)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)
def run():
    parse_home()


if __name__ == '__main__':
    run()