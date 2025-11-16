import telebot
import random
import webbrowser

from telebot import types

bot = telebot.TeleBot("")
api = ''
@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://www.ozon.ru')

@bot.message_handler(commands=['start'])
def get(message):
    m = types.ReplyKeyboardMarkup()
    b = types.KeyboardButton('Да')
    m.row(b)

    bot.send_message(message.from_user.id,f"привет {message.from_user.first_name} {message.from_user.last_name} мне подобрать для тебя игру",reply_markup=m)
    bot.reply_to(message,f"id{message.from_user.id}")

# def on_click(message):
#     if message.text == 'Да':
#         h = random.randint(0, 6)
#         if h == 1:
#             bot.send_message(message.from_user.id, "идите в столовку")
#         if h == 2:
#             bot.send_message(message.from_user.id, "поиграйте в телефон")
#         if h == 3:
#             bot.send_message(message.from_user.id, "поиграйте в бравл")
#         if h == 4:
#             bot.send_message(message.from_user.id, "посидите в классе")
#         if h == 5:
#             bot.send_message(message.from_user.id, "не сидите в классе")
#         if h == 6:
#             bot.send_message(message.from_user.id, "поиграйте в телефон или отправте фото")
#     if message.text == 'удолить':
#         bot.send_message(message.from_user.id, "это прикол")


@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == "Да":
        h=random.randint(0,6)
        if h == 1:
            bot.send_message(message.from_user.id, "пообщяйтесь")
        if h == 2:
            bot.send_message(message.from_user.id, "идите в столовку")
        if h == 3:
            bot.send_message(message.from_user.id, "поиграйте в телефон")
        if h == 4:
            bot.send_message(message.from_user.id, "не сидите в классе")
        if h == 5:
            bot.send_message(message.from_user.id, "поиграйте в телефон или отпавте фото")
        if h == 6:
            bot.send_message(message.from_user.id, "поиграйте в бравл")
    elif message.text == "Привет":
        bot.send_message(message.from_user.id, "привет мне подобрать для тебя игру")
        bot.send_message(message.from_user.id, "напиши привет")

    # else:
    #     bot.send_message(message.from_user.id, "я тебя не понимаю напиши /help")

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    m = types.InlineKeyboardMarkup()
    b =types.InlineKeyboardButton("удолить фото", callback_data='delete')
    b2 =types.InlineKeyboardButton("заменить текст", callback_data='edit')
    m.row(b,b2)
    bot.reply_to(message, 'какое красивое фото!', reply_markup=m)
    bot.register_next_step_handler(message, call_mes)
@bot.callback_query_handler(func=lambda callback: True)
def call_mes(callback):
    if callback.data=='delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id -1)
    if callback.data == 'edit':
        bot.edit_message_text('зачееееееем',callback.message.chat.id, callback.message.message_id)
bot.polling(non_stop=True)

