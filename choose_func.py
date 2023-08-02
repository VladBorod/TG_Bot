from text_for_user import *
import telebot
from bot_token import bot_token

bot = telebot.TeleBot(bot_token)
body_weight = 0.0


def sultasini_calculation(message):
    """Функция расчета сультасина"""

    global body_weight, result
    try:
        body_weight = float(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, text_for_value_error, parse_mode='HTML')
        bot.register_next_step_handler(message, body_weight)

    if body_weight > 0.0:
        result = body_weight * 75
        bot.send_message(message.chat.id, f'<b><u>{round(result, 2)} мг</u></b>', parse_mode='HTML')
        bot.send_message(message.chat.id, f'{text_sultasini_message}', parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, text_for_body_weight_above_zero, parse_mode='HTML')