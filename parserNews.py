from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import time
import json

res = []
linkTinkoff = "https://newssearch.yandex.ru/yandsearch?text=%D1%82%D0%B8%D0%BD%D1%8C%D0%BA%D0%BE%D1%84%D1%84+%D0%B1%D0%B0%D0%BD%D0%BA&rpt=nnews2&grhow=clutop&rel=rel"
linkVtb = "https://newssearch.yandex.ru/yandsearch?text=%D0%B2%D1%82%D0%B1&rpt=nnews2&grhow=clutop&rel=rel"
bankNames = ['Tinkoff', 'Vtb']
bankLinks = [linkTinkoff, linkVtb]
# proxies = {'http': 'http://45.169.163.217:8080',
#         'https': 'http://200.69.84.125:8080'}
# user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) '
#             'Gecko/20100101 Firefox/50.0')


def getHtml(bankLink):
    req = requests.get(bankLink, headers={'User-Agent': UserAgent().chrome})
    # req = requests.get(linkTinkoff)
    return req


def getData(html, counter):
    soup = BeautifulSoup(html.content, 'html.parser')
    # print(soup.prettify())
    allNews = soup.findAll('div', {'class': 'document__title'})
    for news in allNews:
        # time.sleep(4)
        link = news.find('a').get('href')
        bank = {
            'bankName': bankNames[counter],
            'link': link
        } 
        res.append(bank)
        # time.sleep(20)


def main():
    for i in range(0, len(bankLinks)):
        html = getHtml(bankLinks[i])
        getData(html, i)

    with open('res.json', 'w') as file:
        json.dump(res, file, indent=2, ensure_ascii=False)
    print(res)


if __name__ == '__main__':
    main()


# print(soup.prettify())

#soup.find('li', {'class': 'search-item'}).find('div', {'class': 'document i-bem'}).find('h2', {'document__head'}).find('div', {'class': 'document__title'}).find('a', href=True)