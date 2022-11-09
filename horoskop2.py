import requests
from bs4 import BeautifulSoup as bs
URL = 'https://fakty.ua/ru/horoscope/4'
def foo_4():
    r = requests.get(URL)
    soup = bs(r.text , 'html.parser')
    hor = soup.find_all("div", class_="column1")
    clear_hor = [i.text for i in hor]
    return clear_hor[0]
