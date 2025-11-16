import telebot
import requests
import json
bot = telebot.TeleBot("7690542661:AAEoGUVEzrYktzL6EwL6ZTe2_wXAmCr_HWs")
api = '0147b31b0eb679eb71587fb9696979f9'

@bot.message_handler(commands=['start'])
def gor(message):
    bot.send_message(message.from_user.id, "напиши свой город")
@bot.message_handler(content_types=['text'])
def get_text(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if res.status_code ==200:

        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'сейчас {temp}')

        if temp > 5:

            bot.send_message(message.from_user.id, "sunny")
        else:
            bot.send_message(message.from_user.id, "cloudy")
    else:
        bot.send_message(message.from_user.id, "город указон неверно")
bot.polling(non_stop=True, interval=0)