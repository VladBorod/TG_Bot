import telebot
from telebot import types

from medic_force import bot
from text_for_user import *

body_weight = float(0.0)


def sultasini_calculation(message):
    """Функция расчета сультасина"""
    global body_weight
    try:
        body_weight = float(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Введите числовое значение через точку')
        bot.register_next_step_handler(message, sultasini_calculation)
    if body_weight > 0.0:
        result = body_weight * 75
    else:
        bot.send_message(message.chat.id, 'Вес должен быть больше нуля')
    return result, text_sultasini_message

# sul = sultasini_calculation(body_weight)

# Нахуй не нужная функция, но похуй.
# def func_f_more_t_35_w_g_a(callback):
#     """Функция для вывода текста при условных ФР и ГВ более 35 нед."""
#     bot.send_message(callback.message.chat.id, text_for_cbt_supervision)
