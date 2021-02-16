import requests
from bs4 import BeautifulSoup
import re

def request(url):
    req = requests.get(url)
    if req.status_code == 200:
        if 'suwen' in url:
            soup = BeautifulSoup(req.content, 'html.parser')
            pricefind = soup.find(class_="product-detail-price-and-container my-4 clearfix")
            pricefind = pricefind.text
            pricefind = pricefind.strip()
            if len(pricefind) < 10:
                print(pricefind)
            else:
                print(pricefind[28::])
            return pricefind
        else:
            soup = BeautifulSoup(req.content, 'html.parser')
            return soup
    elif req.status_code == 403:
        return('Security Alert, Permission Denied')

