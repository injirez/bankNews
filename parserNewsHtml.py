from bs4 import BeautifulSoup
import time
import json

htmlTinkoff = 'tinkoff.html'
htmlSber = 'sberbank.html'
htmls = [htmlTinkoff, htmlSber]
res = []
def getData():
    for i in range(0, len(htmls)):
        print(htmls[i])
        with open(htmls[i], 'r') as f:
            contents = f.read()
            soup = BeautifulSoup(contents, 'html.parser')
            allNews = soup.findAll('div', {'class': 'document__title'})
            for news in allNews:
                # time.sleep(4)
                link = news.find('a').get('href')
                bank = {
                    'bankName': htmls[i],
                    'link': link
                } 
                res.append(bank)

        # time.sleep(20)
    print(res)
    with open('res.json', 'w') as file:
        json.dump(res, file, indent=2, ensure_ascii=False)

        

getData()


# print(soup.prettify())






#soup.find('li', {'class': 'search-item'}).find('div', {'class': 'document i-bem'}).find('h2', {'document__head'}).find('div', {'class': 'document__title'}).find('a', href=True)