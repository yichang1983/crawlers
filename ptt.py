# # CSS select 寫法 v3
import requests
from bs4 import BeautifulSoup

root_url = 'https://disp.cc/b/'
r = requests.get('https://disp.cc/b/PttHot')
soup = BeautifulSoup(r.text, 'html.parser')

for span in soup.select('div#list span.listTitle'):    #list 意思： #就是id, list 就是條件。 它058的50分鐘有解釋。
    href = span.find('a').get('href')
    if href == '796-59l9':
        break
    url = root_url + href
    title = span.text
    print(f'{title}\n{url}')



# # # CSS select 寫法 v2
# # import requests
# # from bs4 import BeautifulSoup

# # root_url = 'https://disp.cc/b/'
# # r = requests.get('https://disp.cc/b/PttHot')
# # soup = BeautifulSoup(r.text, 'html.parser')

# # for span in soup.select('span.listTitle'):    #span.listTitle 表示span tag 裡包含有class的listTitle.就類似26號的class_= listTitle一樣。span.listTitle.L34.nowrap 也是okay，重點就是找出關鍵的class.
# #     href = span.find('a').get('href')
# #     if href == '796-59l9':
# #         break
# #     url = root_url + href
# #     title = span.text
# #     print(f'{title}\n{url}')


# # CSS select 寫法 v1
# # import requests
# # from bs4 import BeautifulSoup

# # root_url = 'https://disp.cc/b/'
# # r = requests.get('https://disp.cc/b/PttHot')
# # soup = BeautifulSoup(r.text, 'html.parser')

# # spans = soup.select('span.listTitle')  #span.listTitle 表示span tag 裡包含有class的listTitle.就類似26號的class_= listTitle一樣。
# # for span in spans:
# #     href = span.find('a').get('href')
# #     if href == '796-59l9':
# #         break
# #     url = root_url + href
# #     title = span.text
# #     print(f'{title}\n{url}')








# # version 2
# # import requests
# # from bs4 import BeautifulSoup

# # root_url = 'https://disp.cc/b/'
# # r = requests.get('https://disp.cc/b/PttHot')
# # soup = BeautifulSoup(r.text, 'html.parser')
# # spans = soup.find_all('span', class_='L34 nowrap listTitle')
# # for span in spans:
# #     href = span.find('a').get('href')
# #     if href == '796-59l9':
# #         break
# #     url = root_url + href
# #     title = span.text
# #     print(f'{title}\n{url}')

# # example:
# # >>> name = "Fred"
# # >>> f"He said his name is {name}."
# # "He said his name is Fred."











# # version 1
# import requests
# from bs4 import BeautifulSoup

# root_url = 'https://disp.cc/b/'
# r = requests.get('https://disp.cc/b/PttHot')
# soup = BeautifulSoup(r.text, 'html.parser')
# spans = soup.find_all('span', class_='L34 nowrap listTitle')
# for span in spans:
#     url = root_url + span.find('a').get('href')
#     print(url)
#     print(span.text)



# print([s.text for s in spans])