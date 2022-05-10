import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from tabulate import tabulate

pages = np.arange(1,2,1)

for url in pages:
    # site to scrape
    url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=nike+air+force+1&_sacat=0&_pgn="+ str(url)

    # a GET request to site and store it
    page = requests.get(url)

    # parse the HTML content
    soup = BeautifulSoup(page.content, 'html.parser')

    # find all tags and class name
    stocks = soup.findAll('li', class_='s-item s-item__pl-on-bottom')

    # get website's name
    print("\n" + urlparse(url).netloc)
    print("\n" + url)

    # get names
    shoe_names = []
    for stock in stocks:
        shoes = stock.find('h3', class_="s-item__title")
        shoe_names.append(shoes.text)
        #print(shoe_names)

    #get name's description
    shoe_description = []
    for stock in stocks:
        desc = stock.find('span', class_="SECONDARY_INFO")
        shoe_description.append(desc.text)
        #print(shoe_description)

    # get current prices
    current_price = []
    for stock in stocks:
        price = stock.find('span', class_="s-item__price")
        current_price.append(price.text)
        #print(current_price)

    # get url links
    url_list = []
    for url_page in stocks:
        link = url_page.find('a', class_='s-item__link', href=True)
        url_list.append(link['href'])
        #print(url_list)

    # make a dataframe to separate each item to columns/rows
    dataFile = {'Name':shoe_names,'Type':shoe_description,'Price':current_price,'Link':url_list}
    dataShow = {'Name':shoe_names,'Type':shoe_description,'Price':current_price}

    # make data shown in dataframe
    df1 = pd.DataFrame(dataShow)
    df2 = pd.DataFrame(dataFile)

    # ignroe the dollar sign $ to sort it by regex
    df1['Price'] = df1['Price'].replace('[\$]','', regex=True)
    df2['Price'] = df2['Price'].replace('[\$]','', regex=True)

    # show only the name, type, and price
    selection = df1[['Name', 'Type', 'Price']]
    selection = df1.to_markdown(index=False)

    # separate contents to include links
    selection2 = ['Name','Type', 'Price', 'Link']

    # set table standards
    pd.set_option('display.max.rows', 500)
    pd.set_option('display.max.columns', 500)
    pd.set_option('display.width', 1000)

    #print(sort_values)
    print(selection)

    # print info to excel
    #writer = pd.ExcelWriter(r'C:\Users\TEST\Desktop\CMPE-130\ebay.xlsx', engine='xlsxwriter')
    #df2.to_excel(writer, sheet_name='Sheet1')
    #writer.save()

    # print info to csv
    df2.loc[:, selection2].to_csv('ebay.csv')

    # print info to md file
    df2.loc[:, selection2].to_markdown('ebay.md')
