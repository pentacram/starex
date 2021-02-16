import requests
from bs4 import BeautifulSoup
from request import request

def search(data):

    class_list = []
    class_set = set()
    html_tag = ['prc', 'product__price', 'product_price', 'price', "price--content content--default", "product-info-prices-new", "prc-dsc", "prc-slg", "price-wrapper visible"]


    search = {search.name for search in data.find_all()}
    
    for element in tags:
        for i in soup.find_all(element):
            if i.has_attr("class"):
                if len(i['class']) != 0:
                    class_list.append(" ".join(i['class']))

    for tag in range(len(html_tag)):
        cleaner_html = data.find(class_=html_tag[tag])
        if cleaner_html:
            class_set.add(cleaner_html.text)
            return list(class_set)
        else:
            return('Product Nof Found')

def parse(data):

    cleaner_data = []

    for element in range(len(data)):
        if a[i] != " " and "%" not in a[i] and len(a[i]) < 10 and a[i] != '' and "\n" not in a[i]:
            cleaner_data.append(data[element])

    return cleaner_data





    