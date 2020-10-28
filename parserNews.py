from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

linkTinkoff = "https://newssearch.yandex.ru/yandsearch?text=%D1%82%D0%B8%D0%BD%D1%8C%D0%BA%D0%BE%D1%84%D1%84&rpt=nnews2&grhow=clutop"
linkVtb = "https://newssearch.yandex.ru/yandsearch?text=%D0%B2%D1%82%D0%B1&rpt=nnews2&grhow=clutop&rel=rel"
proxies = {'http': 'http://45.169.163.217:8080',
           'https': 'http://200.69.84.125:8080'}
user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) '
              'Gecko/20100101 Firefox/50.0')
htmlTinkoff = '/Users/rodionibragimov/Documents/bankNews/tinkoff.html'


# req = requests.get(linkTinkoff)
# req = requests.get(linkTinkoff, headers={'User-Agent': UserAgent().chrome}, proxies=proxies)
# soup = BeautifulSoup(req.content, 'html.parser')

with open(htmlTinkoff, 'r') as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')

    allNews = soup.findAll('div', {'class': 'document__title'})
    # print(allNews)

    for news in allNews:
        link = news.find('a').get('href')
        print(link)

    # print(soup.prettify())

#soup.find('li', {'class': 'search-item'}).find('div', {'class': 'document i-bem'}).find('h2', {'document__head'}).find('div', {'class': 'document__title'}).find('a', href=True)