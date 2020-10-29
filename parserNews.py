from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import time
from datetime import datetime
import json
from requests.auth import HTTPProxyAuth
from storage import *
from requests import exceptions


# auth = HTTPProxyAuth('Cfamoscow','8u43jl')
# user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) '
#             'Gecko/20100101 Firefox/50.0')


def getHtml(bankLink, proxies):
    req = requests.get(bankLink, headers={'User-Agent': UserAgent().chrome}, proxies=proxies)
    # print(req.status_code)
    return req 
    


def getData(html, counterBankName):
    with open("res.json", "r") as readFile:
        data = json.load(readFile)
    repeatCheck = False
    soup = BeautifulSoup(html.content, 'html.parser')
    # print(soup.prettify())
    time.sleep(5)
    allNews = soup.findAll('div', {'class': 'document__title'})
    if allNews != []:
        for news in allNews:
            time.sleep(6)
            link = news.find('a').get('href')
            bank = {
                'bankName': bankNames[counterBankName],
                'link': link,
                'timestamp': datetime.now().strftime("%d-%m-%Y %H:%M")
            } 
            for a in range(len(data)):
                if bank['link'] == data[a]['link']:
                    print("Error, repeating news: ", bank)
                    repeatCheck = True
            if repeatCheck == False:
                res.append(bank)
            else:
                repeatCheck = False
            with open('res.json', 'w') as file:
                json.dump(res, file, indent=2, ensure_ascii=False)
        else:
            print('Error, yandex banned you')
            
            

            


def main():
    z = 0
    while True:
        for i in range(0, len(bankLinks)):
            if z >= len(allProxies):
                z = 0
            try:
                html = getHtml(bankLinks[i], allProxies[z])
                soup = BeautifulSoup(html.content, 'html.parser')
                allNews = soup.findAll('div', {'class': 'document__title'})
                
                if allNews != []:
                    getData(html, i)
                else:
                    print('Error, yandex banned you, trying next proxies...', allProxies[z])
                    z += 1
            except requests.exceptions.ProxyError:
                print('Bad proxy connection, changing proxy...', allProxies[z])
                z += 1 
            print(z)
            time.sleep(20)

    


if __name__ == '__main__':
    main()


# print(soup.prettify())

#soup.find('li', {'class': 'search-item'}).find('div', {'class': 'document i-bem'}).find('h2', {'document__head'}).find('div', {'class': 'document__title'}).find('a', href=True)