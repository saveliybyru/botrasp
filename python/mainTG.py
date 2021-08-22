'''Helper by Saveliy Burkov is licensed under CC BY-SA 4.0.'''

import secret
import func
import telebot
from telebot import types


ask_today=str(func.today + func.Dej(func.todayd))
ask_tomorrow=str('Завтра ' + func.tomorrow + func.Dej(func.tomorrowd))



#Создание бота

bot = telebot.TeleBot(secret.TOKEN)



#Клавиатуры
startingkb = types.InlineKeyboardMarkup(row_width=2)
up1_button=startingkb.add(types.InlineKeyboardButton(text='Сегодня', callback_data='dej'))
up2_button=startingkb.add(types.InlineKeyboardButton(text='Завтра', callback_data='zav'))
down1_button=startingkb.add(types.InlineKeyboardButton(text='Пожелания и идеи', url=''))


#Обработчики

@bot.message_handler(commands=['start', 'help'])
def send_help(message):
    bot.send_message(message.chat.id, 'Привет!👋 '
                         '\n Я могу подсказать кто дежурит сегодня или завтра '
                         '\nЕсть кнопки и команды: '
                         '\n/dej или кнопка "Сегодня" тебе подскажет дежурных на сегодня '
                         '\n/dejzav или кнопка "Завтра" поможет тебе узнать дежурных на следующий день '
                         '\nТакже свои пожелания и идеи можно написать в канал ',
                   reply_markup=startingkb, disable_web_page_preview= True)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id,)
    answer = ''
    if call.data == 'dej':
        answer = ask_today
    elif call.data == 'zav':
        answer = ask_tomorrow
    bot.send_message(call.message.chat.id, answer)

@bot.message_handler(commands=['dej'])
def pinned(message):
    bot.send_message(message.chat.id, ask_today)


@bot.message_handler(commands=['dejzav'])
def pinnedz(message):
    bot.send_message(message.chat.id, ask_tomorrow)


@bot.message_handler()
def garbage(message):
    bot.send_message(message.chat.id, 'Я могу только дежурных подсказать🥺 '
                         '\nКоманды: /dej и /dejzav '
                         '\nТакже можно почитать описание /help'
                         '\nЕсли чего-то не хватает, то пиши здесь👉 ', disable_web_page_preview= True )


if __name__ == '__main__':
    bot.polling(none_stop=True)