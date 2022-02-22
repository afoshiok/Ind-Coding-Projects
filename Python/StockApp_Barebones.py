import requests
import json
from requests.models import Response
import datetime

try:
    ticker = input('Enter ticker name here(IN ALL CAPS):')
    today = datetime.datetime.now() 
    yesterday = today - datetime.timedelta(days = 1) #API doesn't show stock information for today.
    date_f = yesterday.strftime("%Y-%m-%d")
    date_full = yesterday.strftime("%B %d,%Y")

    url = 'https://api.polygon.io/v3/reference/tickers?ticker={}&active=true&sort=ticker&order=asc&limit=10&apiKey=VapxuwrlubAE4GRJTDkDOiIPjiVdlVE1'.format(ticker)
    r = requests.get(url)
    url2 = 'https://api.polygon.io/v1/open-close/{}/{}?adjusted=true&apiKey=VapxuwrlubAE4GRJTDkDOiIPjiVdlVE1'.format(ticker,date_f)
    r2 = requests.get(url2)


    stock = r.json()
    stock_info = r2.json()

    print('{}({})'.format(stock['results'][0]['name'],stock['results'][0]['ticker']))
    print('--------------------------------------------------------------------------------------------------')
    print('Information for {}:'.format(date_full))
    weekends = ['Saturday', 'Sunday']

    if yesterday.strftime("%A") in weekends:
        print("The markets are not open on the weekends :(\n")
        q1 = input("Do you want to enter an another date?").lower() #Always results in lowercase variable 
        while 'yes' in q1:
         dd = input('Enter new date(YYYY-MM-DD):') 
         new_date = datetime.datetime.strptime(dd, '%Y-%m-%d')
         new_date_f = new_date.strftime("%Y-%m-%d")
         new_date_full = new_date.strftime("%B %d,%Y")
         url3 = 'https://api.polygon.io/v1/open-close/{}/{}?adjusted=true&apiKey=VapxuwrlubAE4GRJTDkDOiIPjiVdlVE1'.format(ticker,new_date_f)
         r3 = requests.get(url3)
         stock_info_nd = r3.json()
         print('Information for {}:'.format(new_date_full))
         print('Opening Price: ${}'.format(stock_info_nd['open']))
         print('Closing Price: ${}\n'.format(stock_info_nd['close']))
         q1 = input("Do you want to enter an another date?").lower()
         #print(stock_info_nd)
        if 'no' in q1:
            print('Ok bye!')
    else: #This prints the info for yesterday.
        print('Opening Price: ${}'.format(stock_info['open']))
        print('Closing Price: ${}'.format(stock_info['close'])) 
        print('\nSee you tomorrow!')
except TypeError:
    print("Stock doesn't exist")


#print(r3.status_code)
yy = yesterday.strftime("%A")
print(yy)




print("hello")

