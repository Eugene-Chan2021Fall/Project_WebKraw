import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# site to scrape
url = "https://www.nike.com/w/air-force-1-shoes-5sj3yzy7ok"

# a GET request to site and store it
page = requests.get(url)

# parse the HTML content
soup = BeautifulSoup(page.content, 'html.parser')

# find all tags and class name
stocks = soup.findAll('div', class_='product-card__body')

# get website's name
print(urlparse(url).netloc)

# get names
shoe_names = []
for stock in stocks:
    shoes = stock.find('div', class_="product-card__title")
    shoe_names.append(shoes.text)
#print(shoe_names)

#get name's description
shoe_description = []
for stock in stocks:
    desc = stock.find('div', class_="product-card__subtitle")
    shoe_description.append(desc.text)

# get current prices
current_price = []
for stock in stocks:
    price = stock.find('div', class_="product-card__price")
    current_price.append(price.text)
#print(current_price)

data = {'Name':shoe_names,'Type':shoe_description,'Price':current_price}
df = pd.DataFrame(data)
df['Price'] = df['Price'].replace('\$|,','', regex=True)
df['Price'] = pd.to_numeric(df['Price'])
sort_values = df.sort_values(by='Price',
                        ascending = True,
                        kind = 'quicksort',
                        ignore_index = True
                        )
print(sort_values)
