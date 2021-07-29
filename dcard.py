

# # CSS select 寫法 v3(# Dcard version 5)
import requests
from bs4 import BeautifulSoup

root_url = 'https://www.dcard.tw'
r = requests.get('https://www.dcard.tw/f')
soup = BeautifulSoup(r.text, 'html.parser')

for span in soup.select('divstylepadding-top h2.tgn9uw-2.jWUdzO'):    #可以把高層和低層的東西配進去條件尋找， div style=padding-top 
    href = span.find('a').get('href')
    if href == '796-59l9':
        break
    url = root_url + href
    title = span.text
    print(f'{title}\n{url}')




# ******************************************************
# CSS select 寫法 v2(# Dcard version 4)
import requests
from bs4 import BeautifulSoup

root_url = 'https://www.dcard.tw'
r = requests.get('https://www.dcard.tw/f')
soup = BeautifulSoup(r.text, 'html.parser')

for span in soup.select('h2.tgn9uw-2.jWUdzO'):    
    href = span.find('a').get('href')
    url = root_url + href
    title = span.text
    print(f'{title}\n{url}')

# ******************************************************
# CSS select 寫法 v1(# Dcard version 3)
# import requests
# from bs4 import BeautifulSoup

# root_url = 'https://www.dcard.tw'
# r = requests.get('https://www.dcard.tw/f')
# soup = BeautifulSoup(r.text, 'html.parser')

# spans = soup.select('h2.tgn9uw-2.jWUdzO')  #h2 表示h2 tag 裡包含有class的tgn9uw-2 and jWUdzO.
# for span in spans:
#     href = span.find('a').get('href')
#     url = root_url + href
#     title = span.text
#     print(f'{title}\n{url}')



# ******************************************************
# Dcard version 2
# import requests
# from bs4 import BeautifulSoup

# root_url = 'https://www.dcard.tw'
# r = requests.get('https://www.dcard.tw/f')
# soup = BeautifulSoup(r.text, 'html.parser')
# spans = soup.find_all('h2', class_='tgn9uw-2 jWUdzO')
# for span in spans:
#     href = span.find('a').get('href')
#     url = root_url + href
#     title = span.text
#     print(f'{title}\n{url}')

# example:
# >>> name = "Fred"
# >>> f"He said his name is {name}."
# "He said his name is Fred."



# ******************************************************
# #Dcard version 1
# import requests
# from bs4 import BeautifulSoup

# root_url = 'https://www.dcard.tw'
# r = requests.get('https://www.dcard.tw/f')
# soup = BeautifulSoup(r.text, 'html.parser')
# spans = soup.find_all('h2', class_='tgn9uw-2 jWUdzO')
# for span in spans:
#     url = root_url + span.find('a').get('href')
#     print(url)
#     print(span.text)