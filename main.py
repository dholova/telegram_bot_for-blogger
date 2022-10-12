import telebot
from telebot import types

bot = telebot.TeleBot('5727769299:AAGJ57dYBWdOUOczmkj8NMiNILrIaayZJUg')


@bot.message_handler(commands=['start', 'help'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    url_btn = types.KeyboardButton(text='Подкасти')
    url_btn1 = types.KeyboardButton(text='Інші відео')
    url_btn11 = types.KeyboardButton(text='Донат')
    url_btn111 = types.KeyboardButton(text='Телеграм канал')

    markup.add(url_btn, url_btn1, url_btn11, url_btn111)

    bot.send_message(message.chat.id, 'Привіт, що хочеш послухати?)', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    markup2 = types.InlineKeyboardMarkup()
    url_btn2 = types.InlineKeyboardButton(text='Подкаст | Розмова з ІТ-новачком', url='https://www.youtube.com/watch?v=GbOQ7sQNDKo')
    markup3 = types.InlineKeyboardMarkup()
    url_btn3 = types.InlineKeyboardButton(text='Поради для новачків в ІТ', url='https://www.youtube.com/watch?v=FrglYc9CLAM&ab_channel=Stasoz')
    url_btn4 = types.InlineKeyboardButton(text='Пару слів про C# і .NET', url='https://www.youtube.com/watch?v=KataDL9X3_o&ab_channel=Stasoz')
    url_btn5 = types.InlineKeyboardButton(text='IaaS, PaaS, SaaS. Різниця', url='https://www.youtube.com/watch?v=I3_T0ELsva8&t&ab_channel=Stasoz')
    url_btn6 = types.InlineKeyboardButton(text='Як працює запит в браузері?', url='https://www.youtube.com/watch?v=NGs0Ug_7i_Y&ab_channel=Stasoz')
    markup4 = types.InlineKeyboardMarkup()
    url_btn7 = types.InlineKeyboardButton(text='Телеграм канал', url='https://t.me/stasozit')

    markup2.add(url_btn2)
    markup3.add(url_btn3, url_btn4, url_btn5, url_btn6)
    markup4.add(url_btn7)

    if message.chat.type == 'private':
        if message.text == 'Подкасти':
            bot.send_message(message.chat.id, 'Оберіть, будь ласка, подкаст для прослуховування😊', reply_markup=markup2)
        elif message.text == 'Інші відео':
            bot.send_message(message.chat.id, 'Оберіть, будь ласка, відео😊', reply_markup=markup3)
        elif message.text == 'Донат':
            bot.send_message(message.chat.id, 'Карта ПриватБанк для донату:')
            bot.send_message(message.chat.id, '5457082227969750')
        elif message.text == 'Телеграм канал':
            bot.send_message(message.chat.id, 'Підпишись, будь ласка, на телеграм канал😊', reply_markup=markup4)


if __name__ == '__main__':
    bot.polling(none_stop=True)