from bs4 import BeautifulSoup as bs
import time
import requests
import winsound
import time
import webbrowser
from datetime import date



def scrape_price(url):
    global price_USD

    page = requests.get(url, timeout=5)

    soup = bs(page.content,features="lxml")

    list_price = [i.text for i in soup.find_all(class_='priceValue')]
    price_str = list_price[0].lstrip("$")
    price_USD = float(price_str)

    return str(price_USD)


def sell_treshold(treshold):
    if price_USD > treshold:
        winsound.Beep(676, 1000)
        time.sleep(2)
        url = "https://youtu.be/dQw4w9WgXcQ"
        webbrowser.open(url,2)


def get_date():
    today = date.today()
    format = str(today.strftime("%B %d, %Y"))

    return format


#get the price of RLC
print(get_date()+ " RLC price : $"+ scrape_price('https://coinmarketcap.com/currencies/rlc/'))

#sell when the RLC price reaches over $11
sell_treshold(11)


#joke
try:    
    sell_treshold(moon)
except NameError:
    print("Keep hoping :)")



