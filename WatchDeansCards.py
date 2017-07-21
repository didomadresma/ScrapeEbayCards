#!/usr/bin/env python36

import string

import requests
from bs4 import BeautifulSoup


url = "https://www.ebay.com/sch/m.html?_nkw=&_armrs=1&_from=&_ssn=deans_cards&_sop=10&_ipg=50&rt=nc"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

card_names = soup.find_all('h3', class_="lvtitle")
card_prices = soup.find_all('li', class_="lvprice prc")


def clean_text(text_dict):
    count = 0
    for rough_text in text_dict:
        text = rough_text.get_text().strip('New listing').lstrip().rstrip()
        text_dict[count] = text
        count += 1

clean_text(card_names)
clean_text(card_prices)

cards = dict(zip(card_names, card_prices))
for card in cards:
    print(card + " : " + cards[card])
