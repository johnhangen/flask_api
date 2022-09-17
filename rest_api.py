from flask import Flask, jsonify
from bs4 import BeautifulSoup
from lxml import etree
import requests
import logging
from urllib.error import HTTPError, URLError
from typing import List

# funtction to web scrape data

def scrapeStockInfo(id:str = "AAPL") -> List[str]:
    HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'}) 

    url = f"https://www.cnbc.com/quotes/{id.upper()}"
    try:
        site = requests.get(url, headers = HEADERS)
    except (URLError,HTTPError) :
        logging.error(f"{url} unable to get requests")
    soup = BeautifulSoup(site.content ,'html.parser')
    dom = etree.HTML(str(soup))
    stockInfo = {"name":dom.xpath('//*[@id="quote-page-strip"]/div[1]/h1/span[1]')[0].text,
        "price":dom.xpath('//*[@id="quote-page-strip"]/div[3]/div[1]/div[2]/span[1]')[0].text}
    #if (stockInfo[0] == None or stockInfo[1] == None):
        #logging.error("xpath not working correctly")
    return stockInfo


app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def hello():
    return "To check the price of a stock just add /stock/ and then your stock ticker to the end of the address"

@app.route('/stocks/<tic>', methods = ['GET'])
def stockConn(tic):
    return jsonify(scrapeStockInfo(tic))

if __name__ == '__main__':
    app.run(debug=True)