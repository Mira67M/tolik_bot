import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot('7764846896:AAEF9LWZ7urLmkpVZs5AUGVMNi9x81Q72AE')

@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://must-see.top/pamyatniki-penzy/')



#parse_mode='html'

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(content_types=['photo']) #если пользователь отправляет файл
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://must-see.top/pamyatniki-penzy/'))
    bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)


bot.polling(none_stop=True)