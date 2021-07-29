import requests
from bs4 import BeautifulSoup


r = requests.get('https://tw.stock.yahoo.com/q/q?s=0056')
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find_all('table')[2]       #找出所有表格，[2]就是第三個表格
    price = table.find_all('td')[2]         #在第三個表格中，[2]就是找出第三個td
    buy_price = price.find_next('td')       #find_next 就是price 的下一個td
    sell_price = buy_price.find_next('td')  #find_next 就是buy_price的下一個td
    print((price.text, buy_price.text, sell_price.text))

