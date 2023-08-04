from text_for_user import *
import telebot
from bot_token import bot_token

bot = telebot.TeleBot(bot_token)
# body_weight = 0.0


def sultasini_calculation(message):
    """Функция расчета сультасина"""
    body_weight = 0.0
    try:
        body_weight = float(message.text.strip())
        if body_weight <= 0.0:
            bot.send_message(message.chat.id, text_for_body_weight_above_zero, parse_mode='HTML')
            return
        elif body_weight > 0.0:
            result = body_weight * 75
            bot.send_message(message.chat.id, f'<b><u>{round(result, 2)} мг</u></b>', parse_mode='HTML')
            bot.send_message(message.chat.id, f'{text_sultasini_message}', parse_mode='HTML')
            return
    except ValueError:
        bot.send_message(message.chat.id, text_for_value_error, parse_mode='HTML')
        bot.register_next_step_handler(message, body_weight)
        return


def ampicillini_calculation(message):
    """Функция расчета ампициллина"""
    body_weight = 0.0
    try:
        body_weight = float(message.text.strip())
        if body_weight <= 0.0:
            bot.send_message(message.chat.id, text_for_body_weight_above_zero, parse_mode='HTML')
            return
        elif body_weight > 0.0:
            result = body_weight * 50
            bot.send_message(message.chat.id, f'<b><u>{round(result, 2)} мг</u></b>', parse_mode='HTML')
            bot.send_message(message.chat.id, f'{text_ampicillini_message}', parse_mode='HTML')
            return
    except ValueError:
        bot.send_message(message.chat.id, text_for_value_error, parse_mode='HTML')
        bot.register_next_step_handler(message, body_weight)
        return


def amikacini_calculation(message):
    """Функция расчета АМИКАЦИНА с кратностью 24-36-48 ч."""
    body_weight = 0.0
    try:
        body_weight = float(message.text.strip())
        if body_weight <= 0.0:
            bot.send_message(message.chat.id, text_for_body_weight_above_zero, parse_mode='HTML')
            return
        elif body_weight > 0.0:
            result = body_weight * 15
            bot.send_message(message.chat.id, f'<b><u>{round(result, 2)} мг</u></b>', parse_mode='HTML')
            return
    except ValueError:
        bot.send_message(message.chat.id, text_for_value_error, parse_mode='HTML')
        bot.register_next_step_handler(message, body_weight)
        return

# Методы МЕРОНЕМА!!!!!!!!
def meronemi_calculation_13(message):
    """Функция расчета Меронема 13 мг"""
    body_weight = 0.0
    try:
        body_weight = float(message.text.strip())
        if body_weight <= 0.0:
            bot.send_message(message.chat.id, text_for_body_weight_above_zero, parse_mode='HTML')
            return
        elif body_weight > 0.0:
            result = body_weight * 13
            bot.send_message(message.chat.id, f'<b><u>{round(result, 2)} мг</u></b>', parse_mode='HTML')
            return
    except ValueError:
        bot.send_message(message.chat.id, text_for_value_error, parse_mode='HTML')
        bot.register_next_step_handler(message, body_weight)
        return


def meronemi_calculation_20(message):
    """Функция расчета Меронема 20 мг"""
    body_weight = 0.0
    try:
        body_weight = float(message.text.strip())
        if body_weight <= 0.0:
            bot.send_message(message.chat.id, text_for_body_weight_above_zero, parse_mode='HTML')
            return
        elif body_weight > 0.0:
            result = body_weight * 20
            bot.send_message(message.chat.id, f'<b><u>{round(result, 2)} мг</u></b>', parse_mode='HTML')
            return
    except ValueError:
        bot.send_message(message.chat.id, text_for_value_error, parse_mode='HTML')
        bot.register_next_step_handler(message, body_weight)
        return


def meronemi_calculation_30(message):
    """Функция расчета Меронема 30 мг"""
    body_weight = 0.0
    try:
        body_weight = float(message.text.strip())
        if body_weight <= 0.0:
            bot.send_message(message.chat.id, text_for_body_weight_above_zero, parse_mode='HTML')
            return
        elif body_weight > 0.0:
            result = body_weight * 30
            bot.send_message(message.chat.id, f'<b><u>{round(result, 2)} мг</u></b>', parse_mode='HTML')
            return
    except ValueError:
        bot.send_message(message.chat.id, text_for_value_error, parse_mode='HTML')
        bot.register_next_step_handler(message, body_weight)
        return


def meronemi_calculation_40(message):
    """Функция расчета Меронема 40 мг"""
    body_weight = 0.0
    try:
        body_weight = float(message.text.strip())
        if body_weight <= 0.0:
            bot.send_message(message.chat.id, text_for_body_weight_above_zero, parse_mode='HTML')
            return
        elif body_weight > 0.0:
            result = body_weight * 40
            bot.send_message(message.chat.id, f'<b><u>{round(result, 2)} мг</u></b>', parse_mode='HTML')
            return
    except ValueError:
        bot.send_message(message.chat.id, text_for_value_error, parse_mode='HTML')
        bot.register_next_step_handler(message, body_weight)
        return


def fluconazoli_calculation_40(message):
    """Функция расчета Флуконазола мг"""
    body_weight = 0.0
    try:
        body_weight = float(message.text.strip())
        if body_weight <= 0.0:
            bot.send_message(message.chat.id, text_for_body_weight_above_zero, parse_mode='HTML')
            return
        elif body_weight > 0.0:
            result_load = body_weight * 12
            result_support = body_weight * 6
            bot.send_message(message.chat.id, f'<b>Нагрузочная:</b> <b><u>{round(result_load, 2)}</u></b>'
                                              f'<b>, поддерживающая:</b> <b><u>{round(result_support, 2)}</u></b>',
                             parse_mode='HTML')
            return
    except ValueError:
        bot.send_message(message.chat.id, text_for_value_error, parse_mode='HTML')
        bot.register_next_step_handler(message, body_weight)
        return


def vancomycini_calculation_10(message):
    """Функция расчета Ванкомицина 10 мг"""
    body_weight = 0.0
    try:
        body_weight = float(message.text.strip())
        if body_weight <= 0.0:
            bot.send_message(message.chat.id, text_for_body_weight_above_zero, parse_mode='HTML')
            return
        elif body_weight > 0.0:
            result = body_weight * 10
            bot.send_message(message.chat.id, f'<b><u>{round(result, 2)} мг</u></b>', parse_mode='HTML')
            return
    except ValueError:
        bot.send_message(message.chat.id, text_for_value_error, parse_mode='HTML')
        bot.register_next_step_handler(message, body_weight)
        return


def vancomycini_calculation_15(message):
    """Функция расчета Ванкомицина 15 мг"""
    body_weight = 0.0
    try:
        body_weight = float(message.text.strip())
        if body_weight <= 0.0:
            bot.send_message(message.chat.id, text_for_body_weight_above_zero, parse_mode='HTML')
            return
        elif body_weight > 0.0:
            result = body_weight * 15
            bot.send_message(message.chat.id, f'<b><u>{round(result, 2)} мг</u></b>', parse_mode='HTML')
            return
    except ValueError:
        bot.send_message(message.chat.id, text_for_value_error, parse_mode='HTML')
        bot.register_next_step_handler(message, body_weight)
        return


def vancomycini_calculation_20(message):
    """Функция расчета Ванкомицина 20 мг"""
    body_weight = 0.0
    try:
        body_weight = float(message.text.strip())
        if body_weight <= 0.0:
            bot.send_message(message.chat.id, text_for_body_weight_above_zero, parse_mode='HTML')
            return
        elif body_weight > 0.0:
            result = body_weight * 20
            bot.send_message(message.chat.id, f'<b><u>{round(result, 2)} мг</u></b>', parse_mode='HTML')
            return
    except ValueError:
        bot.send_message(message.chat.id, text_for_value_error, parse_mode='HTML')
        bot.register_next_step_handler(message, body_weight)
        return