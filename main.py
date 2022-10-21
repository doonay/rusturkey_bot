import requests
from datetime import datetime
import telebot
from auth_data import token

def get_data():
    request = requests.get('https://yobit.net/api/3/ticker/btc_usd')
    response = request.json()
    sell_price = response['btc_usd']['sell']
    now = datetime.now().strftime('%d-%m-%Y %H:%M')
    print(f'{now} BTC price: {sell_price}')
    
def telegram_bot(token):
    bot = telebot.TeleBot(token)
        
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 'Hi!')
    
    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == 'price':
            try:
                request = requests.get('https://yobit.net/api/3/ticker/btc_usd')
                response = request.json()
                sell_price = response['btc_usd']['sell']
                now = datetime.now().strftime('%d-%m-%Y %H:%M')
                bot.send_message(
                    message.chat.id,
                    f'{now} BTC price: {sell_price}'
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    'Damn... Somthing was wrong.'
                )
        else:
            bot.send_message(
                    message.chat.id,
                    'What?'
                )
            
    
    bot.polling()
    
    if __name__ == '__main__':
    #get_data()
    telegram_bot(token)
