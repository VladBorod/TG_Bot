import telebot
from telebot import types

from text_for_user import *
from bot_token import bot_token
from choose_funcs import *

bot = telebot.TeleBot(bot_token)


# Стартовое меню.
# Пользователь может ввести любой текст или нажать старт.
@bot.message_handler(content_types=['text'])
def start(message):
    """"Это стартовый метод!"""
    # Приветствие с пользователем.
    bot.send_message(message.chat.id, f'<b>Привет, '
                                      f'{message.from_user.first_name} {message.from_user.last_name}, '
                                      f'давай рассчитаем антибиотики, </b>',
                     parse_mode='html')
    # Ширина ряда добавления кнопок.
    markup = types.InlineKeyboardMarkup(row_width=3)
    # Новорожденные с ДН без факторов.
    newborn_respiratory_no_risk = types.InlineKeyboardButton(button_newborn_respiratory_no_risk, callback_data='data')
    # НР без КС, но с условными ФР.
    newborn_no_clinic_conditional = types.InlineKeyboardButton(button_newborn_no_clinic_conditional, callback_data='data')
    # НР без КС, но с абсолютными ФР.
    newborn_no_clinic_absolute = types.InlineKeyboardButton(button_newborn_no_clinic_absolute, callback_data='data')
    # Перезапуск.---- не готов!
    restart = types.InlineKeyboardButton(button_restart_text, callback_data='data')
    # Добавление кнопок в ряд шириной 3.
    markup.add(newborn_respiratory_no_risk, newborn_no_clinic_conditional,
               newborn_no_clinic_absolute)
    # Добавление отдельной кнопки перезапуска.
    markup.row(restart)
    # Сообщение о факторах риска.
    bot.send_message(message.chat.id, risc_factors, parse_mode='HTML')
    # Сообщение о выборе варианта.
    bot.send_message(message.chat.id, variant_choose_comment, parse_mode='HTML', reply_markup=markup)


# def on_click(message):
#     if message.text == button_newborn_respiratory_no_risk:
#         bot.send_message(callback.message.chat.id, 'Na')

# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == button_newborn_respiratory_no_risk:
#         markup = types.InlineKeyboardMarkup(row_width=2)
#         more_than_two_risk_factors_rds = types.KeyboardButton(button_more_than_two_risc_factors_rds)
#         markup.add(more_than_two_risk_factors_rds)
        # less_than_two_risk_factors_rds = types.KeyboardButton(button_less_than_two_risc_factors_rds)
        # markup.add(more_than_two_risk_factors_rds, less_than_two_risk_factors_rds)
        # restart = types.KeyboardButton(button_restart_text)
        # markup.row(restart, callback_data='/start')
    # else:
    #     markup = types.ReplyKeyboardMarkup(row_width=1)
    #     restart = types.KeyboardButton(button_restart_text)
    #     markup.add(restart, callback_data='/start')


# Постоянная работа бота.
bot.infinity_polling()
