import config
import telebot
import json
import time
import requests
from telethon import TelegramClient, sync

# bot = telebot.TeleBot(config.token)
# @bot.message_handler(content_types=['text'])


def sendCom():
    repeatCheck = False
    client = TelegramClient(config.sessionName, config.apiId, config.apiHash)
    client.start()
    while True:
        with open("res.json", "r") as readFile:
            data = json.load(readFile)
            for i in range(len(data)):
                for message in client.iter_messages('https://t.me/joinchat/AAAAAFhm7QSwkfehaIs5aw'):
                    if data[i]['bankName']+'\n'+data[i]['link'] == message.text:
                        repeatCheck = True
                
                if repeatCheck == False:
                    requests.get('https://api.telegram.org/bot1412870284:AAF-YWMf4tTEsEUbn_enU4cD_yoWpbEUOpU/sendMessage?chat_id=-1001483140356&text={}\n{}'.format(data[i]['bankName'], data[i]['link']))
                if data[i]['link'] == data[len(data) - 1]['link']:
                    print(data[len(data) - 1]['link'])
                    print("End of file, waiting for more news...")
                    time.sleep(100)

                else:
                    print('Error, repeating message: {}'.format(data[i]['link']))
                    repeatCheck = False
                time.sleep(1)


def main():
    sendCom()





# def sendBot(message):
#     # repeatCheck = False
#     client = TelegramClient(config.sessionName, config.apiId, config.apiHash)
#     client.start()
#     with open("res.json", "r") as readFile:
#         data = json.load(readFile)

#         for i in range(len(data)):
#             with open("usersInfo.json", "r") as readFilee:
#                 usersJson = json.load(readFilee)

#                 user = {
#                     'id': message.chat.id,
#                     'username': message.chat.username
#                 }

#                 for a in range(len(usersJson)):
#                     if 
#                 bot.send_message(message.chat.id, data[i]['link'])
#                 time.sleep(1)
#             with open("usersInfo.json", "w") as filee:
#                 json.dump(user, filee, indent=2, ensure_ascii=False)



if  __name__ == "__main__":
    main()
    # bot.polling(none_stop=True)