import requests
from bs4 import BeautifulSoup

def request(url):
    req = requests.get(url)
    if req.status_code == 200:
        if 'suwen' in url:
            soup = BeautifulSoup(req.content, 'html.parser')
            pricefind = soup.find(class_="product-detail-price-and-container my-4 clearfix")
            return pricefind.text
        else:
            return req.content
    else:
        return('Security Alert, Permission Denied')