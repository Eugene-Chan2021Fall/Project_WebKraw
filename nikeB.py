import pandas as pd
import requests
from bs4 import BeautifulSoup
# site to scrape and makes a GET request to site and store it
page = requests.get("https://www.nike.com/w/air-force-1-shoes-5sj3yzy7ok")

# parse the HTML content
soup = BeautifulSoup(page.content, 'html.parser')

# find all tags and class name
stocks = soup.findAll('div', class_='product-card__body')

# get names
shoe_names = []
for stock in stocks:
    shoes = stock.find('div', class_="product-card__title")
    shoe_names.append(shoes.text)
#print(shoe_names)

# get current prices
current_price = []
for stock in stocks:
    price = stock.find('div', class_="product-card__price")
    current_price.append(price.text)
#print(current_price)

data = {'Name':shoe_names,'Price':current_price}
df = pd.DataFrame(data)
print(df)
