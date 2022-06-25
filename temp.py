from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import winsound
import time
import webbrowser

def pullPrice():
    global price_USD
    global price_GBP
    
    page = requests.get('https://coinmarketcap.com/currencies/rlc/', timeout=5)
    # <Response [200]> - for succesfull connection

    soup = bs(page.content,features="lxml")
    
    #OLD class for RLC
    #list_price = [i.text for i in soup.find_all(class_='priceValue___11gHJ')]
    
    list_price = [i.text for i in soup.find_all(class_='priceValue')]
    
    price_str = list_price[0][1:]

    
    #Convert the price into USD
    price_USD = float(price_str)
    print("USD price is : ",price_USD)
    
    #Convert the price into GBP
    price_GBP = price_USD * 0.71
    print("GBP price is :", price_GBP)
    
    
def compareToLimit(limit):
    if price_GBP > limit:
        winsound.Beep(676, 1000)
        time.sleep(2)
        winsound.Beep(676, 1000)
        time.sleep(2)
        winsound.Beep(676, 1000)
        time.sleep(2)
        winsound.Beep(676, 1000)
        time.sleep(2)
        winsound.Beep(676, 1000)
        time.sleep(2)
        winsound.Beep(676, 1000)
        url = "https://www.youtube.com/watch?v=RN7mbUBzUJw&t=499s&ab_channel=Dieguillo"
        webbrowser.open(url,2)

def start():
    count = 0
    while 1>0:
        count=count+1
        print("Check nr. ", count)
        pullPrice()
        compareToLimit(8.6)
        time.sleep(120)
        print("")
        print("==============================================")
        print("")
    
#start()




def scrape_price(coin, url):
    global price_USD
    global price_GBP

    page = requests.get(url, timeout=5)

    soup = bs(page.content,features="lxml")


    list_price = [i.text for i in soup.find_all(class_='priceValue')]
    price_str = list_price[0].lstrip("$")
    price_USD = float(price_str)
    return price_USD












