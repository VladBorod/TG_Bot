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
    markup = types.InlineKeyboardMarkup(row_width=2)
    # Новорожденные с ДН без факторов.
    newborn_respiratory_no_risk = types.InlineKeyboardButton(text_button_newborn_respiratory_no_risk,
                                                             callback_data='fork_f_t_risk_f_rds')
    # НР без КС, но с условными ФР.
    newborn_no_clinic_conditional = types.InlineKeyboardButton(text_button_newborn_no_clinic_conditional,
                                                               callback_data='fork_f_conditional')
    # НР без КС, но с абсолютными ФР.
    newborn_no_clinic_absolute = types.InlineKeyboardButton(text_button_newborn_no_clinic_absolute,
                                                            callback_data='fork_f_absolute')
    # Добавление верхней кнопки.
    markup.row(newborn_respiratory_no_risk)
    # Добавление двух нижних кнопок.
    markup.add(newborn_no_clinic_conditional,
               newborn_no_clinic_absolute)
    # Сообщение о факторах риска.
    bot.send_message(message.chat.id, text_risc_factors, parse_mode='HTML')
    # Сообщение об условных/абсолютных факторах риска.
    bot.send_message(message.chat.id, text_cond_abs_risc_factor, parse_mode='HTML')
    # Сообщение о выборе варианта.
    bot.send_message(message.chat.id, text_variant_choose, parse_mode='HTML', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data)
def first_fork(callback):
    if callback.data == 'fork_f_t_risk_f_rds':
        markup_rds = types.InlineKeyboardMarkup(row_width=1)
        more_than_two_risk_factors_rds = types.InlineKeyboardButton(text_button_more_than_two_risc_factors_rds,
                                                                    callback_data='fork_f_more_t_r_f_rds')
        less_than_two_risk_factors_rds = types.InlineKeyboardButton(text_button_less_than_two_risc_factors_rds,
                                                                    callback_data='fork_f_less_t_r_f_rds')
        markup_rds.add(more_than_two_risk_factors_rds, less_than_two_risk_factors_rds)
        bot.send_message(callback.message.chat.id, text_fork_for_more_and_less_than_two_risk_factors,
                         parse_mode='HTML', reply_markup=markup_rds)
    elif callback.data == 'fork_f_conditional':
        markup_conditional = types.InlineKeyboardMarkup(row_width=1)
        gestational_age_more_35 = types.InlineKeyboardButton(text_button_more_35_w_g_a,
                                                             callback_data='fork_f_more_t_35_w_g_a')
        gestational_age_less_35 = types.InlineKeyboardButton(text_button_less_35_w_g_a,
                                                             callback_data='fork_f_less_t_35_w_g_a')
        markup_conditional.add(gestational_age_more_35, gestational_age_less_35)
        bot.send_message(callback.message.chat.id, text_for_gestational_age_choose,
                         parse_mode='HTML', reply_markup=markup_conditional)
    elif callback.data == 'fork_f_absolute':
        markup_absolute = types.InlineKeyboardMarkup(row_width=1)
        more_than_two_risk_factors_absolute = types.InlineKeyboardButton(
            text_button_more_than_two_risc_factors_absolute,
            callback_data='fork_f_more_t_2_risc_f_absolute')
        less_than_two_risk_factors_absolute = types.InlineKeyboardButton(
            text_button_less_than_two_risc_factors_absolute,
            callback_data='fork_f_less_t_2_risc_f_absolute')
        markup_absolute.add(more_than_two_risk_factors_absolute, less_than_two_risk_factors_absolute)
        bot.send_message(callback.message.chat.id, text_fork_for_more_and_less_than_two_risk_factors,
                         parse_mode='HTML', reply_markup=markup_absolute)



# Постоянная работа бота.
bot.infinity_polling()
