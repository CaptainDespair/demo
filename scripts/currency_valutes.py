import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'xml')


def get_current_usd_rate():
    usd_rater = soup.find('Valute', {'ID': 'R01235'})\
                         .find('Value')\
                         .text
    usd_rate = usd_rater.replace(',' , '.')
    return float(usd_rate)


def get_current_eur_rate():
    euro_rater = soup.find('Valute', {'ID': 'R01239'})\
                         .find('Value')\
                         .text    
    euro_rate = euro_rater.replace(',' , '.')             
    return float(euro_rate)


if __name__ == '__main__':
    print(get_current_eur_rate(), get_current_usd_rate())