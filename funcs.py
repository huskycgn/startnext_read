import requests
from bs4 import BeautifulSoup
import cred
import telebot
from datetime import datetime


def get_startnext_amount():
    site = 'https://www.startnext.com/rhein-metal/pinnwand#/'
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    header = { 'User-Agent': useragent }
    website = requests.get(url=site, headers=header)

    soup = BeautifulSoup(website.text, 'html.parser')

    result = soup.find(id='cf-app-funding-numbers-counter')

    amount = result.find('span').get_text()[ :-2 ].strip()
    return str(amount)


def send_message(message):
    bot = telebot.TeleBot(token=cred.TOKEN)
    bot.send_message(chat_id=cred.CHAT_ID, text=message)


def run_program():
    startvalue = get_startnext_amount()
    newvalue = get_startnext_amount()
    if newvalue != startvalue:
        send_message(f'Betrag ist jetzt {newvalue} €')
        # print(f'Betrag ist jetzt {newvalue} €')
    print(datetime.now())
    print(f'Start value: {startvalue} €')
    print(f'Current value: {newvalue} €')
    startvalue = newvalue

# end_message('Betrag ist jetzt 5.175 €')
