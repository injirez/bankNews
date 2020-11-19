from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import time
from datetime import datetime
import json
from requests.auth import HTTPProxyAuth
import config
from requests import exceptions



# user_agent = ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) '
#             'Gecko/20100101 Firefox/50.0')


def getHtml(bankLink, proxies):
    # auth = HTTPProxyAuth("rYvfHywqUz", "T7mJ0QtwVR")
    # auth = HTTPProxyAuth("Baupwu", "pD0rl9nJ4V")
    req = requests.get(bankLink, headers={'User-Agent': UserAgent().chrome}, proxies=proxies)
    print(req.status_code)
    return req 
    


def getData(html, counterBankName, counterProxy):
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
                    'bankName': config.bankNames[counterBankName],
                    'link': link,
                    'timestamp': datetime.now().strftime("%d-%m-%Y %H:%M")
                } 

                for a in range(len(data)):
                    if bank['link'] == data[a]['link']:
                        print("Error, repeating news: ", bank)
                        repeatCheck = True
                if repeatCheck == False:
                    config.res.append(bank)
                else:
                    repeatCheck = False
                with open('res.json', 'w') as file:
                    json.dump(config.res, file, indent=2, ensure_ascii=False)
        else:
            print('Error, yandex banned you, trying next proxies...', config.allProxies[counterProxy])
            counterProxy += 1
        readFile.close()

        return counterProxy
            
            

            


def main():
    z = 0
    while True:
        for i in range(0, len(config.bankLinks)):
            try:
                html = getHtml(config.bankLinks[i], config.allProxies[z])
                chok = getData(html, i, z)
                time.sleep(200)
                z = chok
            except requests.exceptions.ProxyError:
                print('Bad proxy connection, changing proxy...', config.allProxies[z])
                # z += 1
                time.sleep(18000)
            if z >= len(config.allProxies):
                z = 0
            if i >= len(config.bankLinks):
                i = 0
            # print(chok)
            # print(z)
            time.sleep(20)

    


if __name__ == '__main__':
    main()


# print(soup.prettify())

#soup.find('li', {'class': 'search-item'}).find('div', {'class': 'document i-bem'}).find('h2', {'document__head'}).find('div', {'class': 'document__title'}).find('a', href=True)