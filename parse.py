import requests
from bs4 import BeautifulSoup
from request import request

def search(data):

    class_list = []
    class_set = set()
    html_tag = ['prc', 'product__price', 'product_price', 'price', "price--content content--default", "product-info-prices-new", "prc-dsc", "prc-slg", "price-wrapper visible"]
    search = {search.name for search in data.find_all()}
    
    for element in search:
        for i in data.find_all(element):
            if i.has_attr("class"):
                if len(i['class']) != 0:
                    class_list.append(" ".join(i['class']))

    for element in class_list:
        if 'prc' in element or 'product__price' in element or 'product_price' in element or 'price' in element:
            s = data.find(class_=element)
            class_set.add(s.text)
    
    return list(class_set)

def parse(data):
    cleaner_data = []

    for element in range(len(data)):
        if data[element] != " " and "%" not in data[element] and len(data[element]) < 10 and data[element] != '' and "\n" not in data[element]:
            cleaner_data.append(data[element])

    return sorted(cleaner_data)[0]





    