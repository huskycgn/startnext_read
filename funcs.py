import requests
from bs4 import BeautifulSoup
import cred
import telebot


def get_startnext_amount():
    site = 'https://www.startnext.com/rhein-metal/pinnwand#/'
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    header = { 'User-Agent': useragent }
    website = requests.get(url=site, headers=header)

    soup = BeautifulSoup(website.text, 'html.parser')

    result = soup.find(id='cf-app-funding-numbers-counter')

    amount = float(result.find('span').get_text()[ :-2 ].replace('.', ''))

    return amount


def send_message(message):
    bot = telebot.TeleBot(token=cred.TOKEN)
    bot.send_message(chat_id=cred.CHAT_ID, text=message)
