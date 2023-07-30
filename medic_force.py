import telebot
from telebot import types

from text_for_user import *
from bot_token import bot_token
from choose_funcs import *

bot = telebot.TeleBot(bot_token)


# Стартовое меню.
# Пользователь может ввести любой текст или нажать старт.
@bot.message_handler(commands=['start'])
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
    newborn_respiratory_no_risk = types.InlineKeyboardButton(button_newborn_respiratory_no_risk, callback_data='data1')
    # НР без КС, но с условными ФР.
    newborn_no_clinic_conditional = types.InlineKeyboardButton(button_newborn_no_clinic_conditional, callback_data='data2')
    # НР без КС, но с абсолютными ФР.
    newborn_no_clinic_absolute = types.InlineKeyboardButton(button_newborn_no_clinic_absolute, callback_data='data3')
    # Добавление кнопок в ряд шириной 3.
    markup.add(newborn_respiratory_no_risk, newborn_no_clinic_conditional,
               newborn_no_clinic_absolute)
    # Сообщение о факторах риска.
    bot.send_message(message.chat.id, text_risc_factors, parse_mode='HTML')
    # Сообщение об условных/абсолютных факторах риска.
    bot.send_message(message.chat.id, text_cond_abs_risc_factor, parse_mode='HTML')
    # Сообщение о выборе варианта.
    bot.send_message(message.chat.id, text_variant_choose, parse_mode='HTML', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'data1':
        markup = types.InlineKeyboardMarkup(row_width=2)
        more_than_two_risk_factors_rds = types.InlineKeyboardButton(button_more_than_two_risc_factors_rds)
        less_than_two_risk_factors_rds = types.InlineKeyboardButton(button_more_than_two_risc_factors_rds)
        markup.add(more_than_two_risk_factors_rds)
        markup.add(less_than_two_risk_factors_rds)
        bot.send_message(callback.message.chat.id, 'Whats next')
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
