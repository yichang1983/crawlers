import requests
from bs4 import BeautifulSoup
import pandas as pd
data = []
r = requests.get('https://chart.capital.com.tw/Chart/TWII/TAIEX11.aspx')
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'lxml')      #lxml 指用它來分析，它就是類似html.parser，但不同的東西。
    tables = soup.find_all('table', attrs={'cellpadding': '2'})   #在table 的同一行裡都是attribute,所以用字典的方式來找出cellpadding. 全部的意思是找出table 裡面有cellpadding=2的東西
    # print(tables[0])
    for table in tables:
        trs = table.find_all('tr')
        for tr in trs:
            date, value, price = [td.text for td in tr.find_all('td')]
            if date == '日期':
                continue
            data.append([date, value, price])
df = pd.DataFrame(data, columns=['日期', '買賣超金額','台指期'])
df.to_csv('big_eight.csv')
df.to_excel('big_eight.xlsx')
df.to_html('big_eight.html')
# print(data)







#****************************************************************
# import requests
# from bs4 import BeautifulSoup


# r = requests.get('https://chart.capital.com.tw/Chart/TWII/TAIEX11.aspx')
# if r.status_code == requests.codes.ok:
#     soup = BeautifulSoup(r.text, 'lxml')      #lxml 指用它來分析，它就是類似html.parser，但不同的東西。
#     # print(soup.prettify())                    #查看是否有把整個網印回傳。

#     tables = soup.find_all('table', attrs={'cellpadding': '2'})   #在table 的同一行裡都是attribute,所以用字典的方式來找出cellpadding. 全部的意思是找出table 裡面有cellpadding=2的東西
#     # print(tables[0])
#     for table in tables:
#         trs = table.find_all('tr')
#         for tr in trs:
#             tds = tr.find_all('td')
#             print(tds)
