import pandas as pd
import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from tabulate import tabulate

# site to scrape
url = "https://www.nike.com/w/air-force-1-shoes-5sj3yzy7ok"

# a GET request to site and store it
page = requests.get(url)

# parse the HTML content
soup = BeautifulSoup(page.content, 'html.parser')

# find all tags and class name
stocks = soup.findAll('div', class_='product-card__body')

# get website's name
print("\n" + urlparse(url).netloc)
print("\n" + url)

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
    # print(shoe_description)

# get current prices
current_price = []
for stock in stocks:
    price = stock.find('div', class_="product-card__price")
    current_price.append(price.text)
    #print(current_price)

# get url list
url_list = []
for url_page in stocks:
    link = url_page.find('a', class_="product-card__img-link-overlay", href = True)
    url_list.append(link['href'])
    # print(url_list)

# have a file be shown at terminal and have another file have the url's inside file
dataFile = {'Name':shoe_names,'Type':shoe_description,'Price':current_price,'Link':url_list}
dataShow = {'Name':shoe_names,'Type':shoe_description,'Price':current_price}

# convert data to dataframe
df1 = pd.DataFrame(dataShow)
df2 = pd.DataFrame(dataFile)

# get rid of dollar sign $
df1['Price'] = df1['Price'].replace('\$|','', regex=True)
df2['Price'] = df2['Price'].replace('\$|','', regex=True)

# put dataframe to markdown table
selection = df1[['Name', 'Type', 'Price']]
selection = df1.to_markdown(index = False)

# separate contents to include links
selection2 = ['Name','Type', 'Price', 'Link']

# set table standards
pd.set_option('display.max.rows', 500)
pd.set_option('display.max.columns', 500)
pd.set_option('display.width', 1000)

print(selection)

# make a md file of the name, type, price, and url link of each item
df2.loc[:, selection2].to_csv('nike.csv')
