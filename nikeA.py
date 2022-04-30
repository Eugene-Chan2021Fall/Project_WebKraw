import requests
from bs4 import BeautifulSoup
# site to scrape
url = "https://www.nike.com/w/air-force-1-shoes-5sj3yzy7ok"

# make a GET request to site and store it
response = requests.get(url)

# parse the HTML content
html_soup = BeautifulSoup(response.text, 'html.parser')

# find all tags and class name
products = html_soup.findAll('div', class_="product-card__body")

for product in products:
    # get product's name
    titleName = product.find("div", class_="product-card__title")
    print("Title: " + titleName.text)

    # get product's price
    priceProduct = product.find("div", class_="product-card__price")
    print("Price: " + priceProduct.text)
