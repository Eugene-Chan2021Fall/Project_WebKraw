import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from tabulate import tabulate

pages = np.arange(1,2,1)

for url in pages:

        # site to scrape
        url = "https://www.footlocker.com/category/shoes/nike/air-force-1.html?currentPage=" + str(url)

        # get website's domain name
        print("\n" + urlparse(url).netloc)
        print("\n" + url)

        # a GET request to site and store it
        req = requests.get(url).content

        # parse the HTML content
        soup = BeautifulSoup(req, 'html.parser')

        # find all tags and class name
        stocks = soup.findAll('li', class_='product-container col')

        # get names
        shoe_names = []
        for stock in stocks:
            shoes = stock.find('span', class_="ProductName-primary")
            shoe_names.append(shoes.text)
            # print(shoe_names)

        # get name's description
        shoe_description = []
        for stock in stocks:
            desc = stock.find('span', class_="ProductName-alt")
            shoe_description.append(desc.text)
            # print(shoe_description)

        # get current prices
        current_price = []
        for stock in stocks:
            if stock.find('span',class_="ProductPrice-final"):
                price = stock.find('span',class_="ProductPrice-final")
                current_price.append(price.text)
                current_price.append(price.text)
            elif stock.find('span',class_="ProductPrice"):
                price = stock.find('span',class_="ProductPrice")
                current_price.append(price.text)
                # print(current_price)

        # get url list
        url_list = []
        for url_page in stocks:
            link = url_page.find('a', class_='ProductCard-link', href = True)
            url_list.append(link['href'])
            # print(url_list)

        # have a file be shown at terminal and have another file have the url's inside file
        dataFile = {'Name':shoe_names,'Type':shoe_description,'Price':current_price,'Link':url_list}
        dataShow = {'Name':shoe_names,'Type':shoe_description,'Price':current_price}
        # convert data to dataframe
        df1 = pd.DataFrame(dataShow)
        df2 = pd.DataFrame(dataFile)

        # get rid of the dollar sign $
        df1['Price'] = df1['Price'].replace('[\$,]','', regex=True)
        df2['Price'] = df2['Price'].replace('[\$,]','', regex=True)

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
        df2.loc[:, selection2].to_markdown('footlocker.md')
