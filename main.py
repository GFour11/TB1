import telebot
import requests
from telebot import types
import random
from wether import city
from wether import open_weather_token
from wether import get_weather

from bs4 import BeautifulSoup as bs
from horoskop2 import URL
from horoskop2 import foo_4



def foo_1():
    file= open('11.txt', 'r', -1, 'utf-8')
    data = file.read()
    data = data.split("\n")
    j=random.choice(data)
    return j
def foo_2():
    file= open('2.txt', 'r', -1, 'utf-8')
    data = file.read()
    data = data.split("\n")
    j=random.choice(data)
    return j
bot = telebot.TeleBot('5729184387:AAHdmR4kSEF50vqSxzKZTF-l3sABL1Cq16Y')
@bot.message_handler(commands =['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привіт! \U0001F44B Розробив невеличкого бота для тебе.\nЩоб розпочати натисни /go')
@bot.message_handler(commands =['go'])
def buttons (message):
    markup = types.ReplyKeyboardMarkup()
    compl = types.KeyboardButton("Отримати комплімент")
    motivation = types.KeyboardButton("Заряд мотивації")
    weather = types.KeyboardButton("Погода в Хельмонді")
    xxx = types.KeyboardButton("Запит на щось хтиве")
    numfour = types.KeyboardButton("Гороскоп")

    markup.add(compl,motivation, weather, xxx,numfour)
    bot.send_message(message.chat.id, "Маю кнопочки для тебе1F4CC\n"
                                      "Інструкція:\n\n"
                                      '-Клацяй "Отримати комплімент", щоб трошки підняти собі настрій\U0000263A \n'
                                      '-Натисни \U0001F4AA"Заряд мотивації"\U0001F4AA, аби збадьорити свідомість!\n'
                                      '-Тицьни \U000026C8"Погода в Хельмонді"\U000026C8 щоб дізнатись, що на вулиці, не виходячи з хижі! \n'
                                      '-Якщо натиснути "Запит на щось хтиве" тоді я побачу твій запит.\n'
                                      '-Також можеш натиснути \U0000264B"Гороскоп"\U0000264B щоб отримати свіженького гороскопа.\n', reply_markup=markup )
@bot.message_handler()
def get_user_txt(message):
    if message.text == "Погода в Хельмонді":
        k=get_weather(city,open_weather_token)
        bot.send_message(message.chat.id, f"{k}" )
    elif message.text == "Отримати комплімент":
        k=foo_1()
        bot.send_message(message.chat.id, f"{k}")
    elif message.text == "Запит на щось хтиве":
        a = f'@{message.chat.username}'
        bot.send_message(message.chat.id, "Запит відправлено \U0001F609")
        bot.send_message(466378150, f"Отримано запит на щось хтиве від @{a}")
    elif message.text =="Заряд мотивації":
        l = foo_2()
        bot.send_message(message.chat.id, f"{l}")
    elif message.text =="Гороскоп":
        m = foo_4()
        bot.send_message(message.chat.id, f"Ось тобі гороскоп на день:\n\n {m}")
    else:
        bot.send_message(message.chat.id, "Баба глуха як тетеря! Краще тицяй в кнопочки \U0001F447")







bot.polling(none_stop=True)