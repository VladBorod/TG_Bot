import telebot
from telebot import types

from text_for_user import *
from bot_token import bot_token
from choose_func import *

bot = telebot.TeleBot(bot_token)


# Стартовое меню.
# Пользователь может ввести любой текст или нажать старт.
@bot.message_handler(commands=['antibiotics'])
def start(message):
    """"Это стартовый метод!"""
    # Приветствие с пользователем.
    bot.send_message(message.chat.id, f'<b>Здравствуйте, '
                                      f'{message.from_user.first_name} {message.from_user.last_name}, '
                                      f'давайте рассчитаем антибиотики! </b>',
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
    # Смена антибактериальной терапии.
    newborn_antibiotics_change = types.InlineKeyboardButton(text_button_newborn_antibchange,
                                                            callback_data='antibiotics_change')
    # Ранний сепсис.
    newborn_sepsis = types.InlineKeyboardButton(text_button_newborn_sepsis, callback_data='sepsis')
    # Добавление верхней кнопки.
    markup.row(newborn_respiratory_no_risk)
    # Добавление двух нижних кнопок.
    markup.add(newborn_no_clinic_conditional,
               newborn_no_clinic_absolute)
    markup.row(newborn_antibiotics_change)
    markup.row(newborn_sepsis)
    # Сообщение о факторах риска.
    bot.send_message(message.chat.id, text_risc_factors, parse_mode='HTML')
    # Сообщение об условных/абсолютных факторах риска.
    bot.send_message(message.chat.id, text_cond_abs_risc_factor, parse_mode='HTML')
    # Сообщение о выборе варианта.
    bot.send_message(message.chat.id, text_variant_choose, parse_mode='HTML', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data)
def first_fork(callback):
    # ДН без факторов риска и дальнейшая вилка.
    if callback.data == 'fork_f_t_risk_f_rds':
        markup_rds = types.InlineKeyboardMarkup(row_width=1)
        # Менее 2-х факторов риска.
        less_than_two_risk_factors_rds = types.InlineKeyboardButton(text_button_less_than_two_risc_factors_rds,
                                                                    callback_data='fork_f_less_2_r_f_rds')
        # Более 2-х факторов риска.
        more_than_two_risk_factors_rds = types.InlineKeyboardButton(text_button_more_than_two_risc_factors_rds,
                                                                    callback_data='fork_f_more_2_r_f_rds')
        # Менее, Более.
        markup_rds.add(less_than_two_risk_factors_rds, more_than_two_risk_factors_rds)
        bot.send_message(callback.message.chat.id, text_for_newborn_with_rds_first_day,
                         parse_mode='HTML')
        bot.send_message(callback.message.chat.id, text_fork_for_more_and_less_than_two_risk_factors,
                         parse_mode='HTML', reply_markup=markup_rds)
    # Условные факторы риска и дальнейшая вилка.
    elif callback.data == 'fork_f_conditional':
        markup_conditional = types.InlineKeyboardMarkup(row_width=1)
        # Более 35 нед. г.в.
        gestational_age_more_35 = types.InlineKeyboardButton(text_button_more_35_w_g_a,
                                                             callback_data='fork_f_more_t_35_w_g_a')
        # Менее 35 нед. г.в.
        gestational_age_less_35 = types.InlineKeyboardButton(text_button_less_35_w_g_a,
                                                             callback_data='fork_f_less_t_35_w_g_a')
        # Более, Менее
        markup_conditional.add(gestational_age_more_35, gestational_age_less_35)
        bot.send_message(callback.message.chat.id, text_for_gestational_age_choose,
                         parse_mode='HTML', reply_markup=markup_conditional)
    # Абсолютные факторы риска и дальнейшая вилка.
    elif callback.data == 'fork_f_absolute':
        markup_absolute = types.InlineKeyboardMarkup(row_width=1)
        # Менее 2-х абсолютных факторов риска.
        less_than_two_risk_factors_absolute = types.InlineKeyboardButton(
            text_button_less_than_two_risc_factors_absolute,
            callback_data='fork_f_less_t_2_risc_f_absolute')
        # Более 2-х абсолютных факторов риска.
        more_than_two_risk_factors_absolute = types.InlineKeyboardButton(
            text_button_more_than_two_risc_factors_absolute,
            callback_data='fork_f_more_t_2_risc_f_absolute')
        markup_absolute.add(less_than_two_risk_factors_absolute, more_than_two_risk_factors_absolute)
        bot.send_message(callback.message.chat.id, text_for_cbt_supervision_and_next_fork,
                         parse_mode='HTML')
        bot.send_message(callback.message.chat.id, text_fork_for_more_and_less_than_two_risk_factors,
                         parse_mode='HTML', reply_markup=markup_absolute)
    # Первый СТОП исходя из оценки гестационного возраста (более 35 недель или
    # отсутствия лабораторных показателей) и отсутствия симптомов.
    elif callback.data == 'fork_f_more_t_35_w_g_a':
        # Сообщение о назначении КАК и клиническом наблюдении.
        bot.send_message(callback.message.chat.id, text_for_cbt_supervision,
                         parse_mode='HTML')
    elif callback.data == 'fork_f_less_t_2_risc_f_absolute':
        # Сообщение о назначении КАК и клиническом наблюдении.
        bot.send_message(callback.message.chat.id, text_for_cbt_supervision,
                         parse_mode='HTML')
    # Вилка на переход из 35 нед. г.в. или переход из абсолютных факторов риска.
    elif callback.data == 'fork_f_less_t_35_w_g_a':
        markup_conditional_less_35_w_g_a = types.InlineKeyboardMarkup(row_width=1)
        less_t_two_risc_factors_less_35_w_g_a = types.InlineKeyboardButton(text_less_t_two_risc_factors_less_35_w_g_a,
                                                                    callback_data='fork_f_more_t_35_w_g_a')
        more_t_two_risc_factors_less_35_w_g_a = types.InlineKeyboardButton(text_more_t_two_risc_factors_less_35_w_g_a,
                                                                    callback_data='more_than_2_r_f_less_35_w')
        markup_conditional_less_35_w_g_a.add(less_t_two_risc_factors_less_35_w_g_a,
                                             more_t_two_risc_factors_less_35_w_g_a)
        bot.send_message(callback.message.chat.id, text_for_cbt_supervision_and_next_fork,
                         parse_mode='HTML', reply_markup=markup_conditional_less_35_w_g_a)
    # Переход к назначению антибактериальной монотерапии!
    elif callback.data == 'fork_f_less_2_r_f_rds':
        markup_less_than_two_r_f_rds = types.InlineKeyboardMarkup(row_width=1)
        # Кнопка монотерапии Сультасином.
        go_to_prescribe_monotherapy_sultas = types.InlineKeyboardButton(text_button_to_prescribe_monotherapy_sultas,
                                                                 callback_data='prescribe_mono_therapy_sultas')
        go_to_prescribe_monotherapy_ampi = types.InlineKeyboardButton(text_button_to_prescribe_monotherapy_ampi,
                                                                        callback_data='prescribe_mono_therapy_ampi')
        markup_less_than_two_r_f_rds.add(go_to_prescribe_monotherapy_sultas, go_to_prescribe_monotherapy_ampi)
        bot.send_message(callback.message.chat.id, text_for_prescribing_an_antibiotic,
                         parse_mode='HTML', reply_markup=markup_less_than_two_r_f_rds)
    # Переход к методу для назначения монотерапии Сультасином!
    elif callback.data == 'prescribe_mono_therapy_sultas':
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
        bot.register_next_step_handler(callback.message, sultasini_calculation)
    # Переход к методу для назначения монотерапии ампициллином!
    elif callback.data == 'prescribe_mono_therapy_ampi':
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
        bot.register_next_step_handler(callback.message, ampicillini_calculation)
    # Переход к стартовой АБ терапии двумя антибиотиками.
    elif callback.data == 'fork_f_more_2_r_f_rds':
        markup_more_than_two_r_f_rds = types.InlineKeyboardMarkup(row_width=1)
        go_to_prescribe_amikacini = types.InlineKeyboardButton(text_button_to_prescribe_amikacini,
                                                               callback_data='prescribe_amikacini')
        markup_more_than_two_r_f_rds.add(go_to_prescribe_amikacini)
        bot.send_message(callback.message.chat.id, text_for_prescribing_an_antibiotic_duo, parse_mode='HTML',
                         reply_markup=markup_more_than_two_r_f_rds)
    elif callback.data == 'more_than_2_r_f_less_35_w':
        markup_more_than_two_r_f_rds = types.InlineKeyboardMarkup(row_width=1)
        go_to_prescribe_amikacini = types.InlineKeyboardButton(text_button_to_prescribe_amikacini,
                                                               callback_data='prescribe_amikacini')
        markup_more_than_two_r_f_rds.add(go_to_prescribe_amikacini)
        bot.send_message(callback.message.chat.id, text_for_prescribing_an_antibiotic_duo, parse_mode='HTML',
                         reply_markup=markup_more_than_two_r_f_rds)
    elif callback.data == 'fork_f_more_t_2_risc_f_absolute':
        markup_more_than_two_r_f_rds = types.InlineKeyboardMarkup(row_width=1)
        go_to_prescribe_amikacini = types.InlineKeyboardButton(text_button_to_prescribe_amikacini,
                                                               callback_data='prescribe_amikacini')
        markup_more_than_two_r_f_rds.add(go_to_prescribe_amikacini)
        bot.send_message(callback.message.chat.id, text_for_prescribing_an_antibiotic_duo, parse_mode='HTML',
                         reply_markup=markup_more_than_two_r_f_rds)
    elif callback.data == 'prescribe_amikacini':
        markup_amikacini_fork_f_gestage = types.InlineKeyboardMarkup(row_width=1)
        # Кратность каждые 24 часа.
        gesage_35_more = types.InlineKeyboardButton(text_button_gesage_35_more,
                                                    callback_data='amik_multiplicity_24')
        gesage_30_34_postcon_8 = types.InlineKeyboardButton(text_button_gesage_30_34_postcon_8,
                                                            callback_data='amik_multiplicity_24')
        gesage_less_29_postcon_29 = types.InlineKeyboardButton(text_button_gesage_less_29_postcon_29,
                                                               callback_data='amik_multiplicity_24')
        # Кратность каждые 36 часов.
        gesage_30_34_postcon_0 = types.InlineKeyboardButton(text_button_gesage_30_34_postcon_0,
                                                            callback_data='amik_multiplicity_36')
        gesage_less_29_postcon_8_28 = types.InlineKeyboardButton(text_button_gesage_less_29_postcon_8_28,
                                                                 callback_data='amik_multiplicity_36')
        # Кратность каждые 48 часов
        gesage_less_29_postcon_0_7 = types.InlineKeyboardButton(text_button_gesage_less_29_postcon_0_7,
                                                                callback_data='amik_multiplicity_48')
        go_to_second_antibiotic_in_combotherapy = types.InlineKeyboardButton(
            text_button_second_antibiotic_in_combotherapy,
            callback_data='second_antibiotic_in_combitherapy')
        markup_amikacini_fork_f_gestage.add(gesage_35_more,
                                            gesage_30_34_postcon_0,
                                            gesage_30_34_postcon_8,
                                            gesage_less_29_postcon_0_7,
                                            gesage_less_29_postcon_8_28,
                                            gesage_less_29_postcon_29,
                                            go_to_second_antibiotic_in_combotherapy)
        bot.send_message(callback.message.chat.id, text_for_gestational_age,
                         parse_mode='HTML', reply_markup=markup_amikacini_fork_f_gestage)

    elif callback.data == 'amik_multiplicity_24':
        bot.register_next_step_handler(callback.message, amikacini_calculation)
        bot.send_message(callback.message.chat.id, text_f_amik_mult_24, parse_mode='HTML')
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
    elif callback.data == 'amik_multiplicity_36':
        bot.register_next_step_handler(callback.message, amikacini_calculation)
        bot.send_message(callback.message.chat.id, text_f_amik_mult_36, parse_mode='HTML')
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
    elif callback.data == 'amik_multiplicity_48':
        bot.register_next_step_handler(callback.message, amikacini_calculation)
        bot.send_message(callback.message.chat.id, text_f_amik_mult_48, parse_mode='HTML')
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
    elif callback.data == 'second_antibiotic_in_combitherapy':
        markup_second_antibiotic_combitherapy = types.InlineKeyboardMarkup(row_width=1)
        # Кнопка монотерапии Сультасином.
        go_to_prescribe_sultas_combi = types.InlineKeyboardButton(text_button_to_prescribe_monotherapy_sultas,
                                                                 callback_data='prescribe_combi_therapy_sultas')
        go_to_prescribe_ampi_combi = types.InlineKeyboardButton(text_button_to_prescribe_monotherapy_ampi,
                                                                        callback_data='prescribe_combi_therapy_ampi')
        markup_second_antibiotic_combitherapy.add(go_to_prescribe_sultas_combi, go_to_prescribe_ampi_combi)
        bot.send_message(callback.message.chat.id, text_for_prescribing_an_antibiotic,
                         parse_mode='HTML', reply_markup=markup_second_antibiotic_combitherapy)
        # Переход к методу для назначения вторым Сультасином!
    elif callback.data == 'prescribe_combi_therapy_sultas':
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
        bot.register_next_step_handler(callback.message, sultasini_calculation)
    # Переход к методу для назначения вторым ампициллином!
    elif callback.data == 'prescribe_combi_therapy_ampi':
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
        bot.register_next_step_handler(callback.message, ampicillini_calculation)

    elif callback.data == 'dynamics':
        markup_dynamics = types.InlineKeyboardMarkup(row_width=1)
        dynamics_decision = types.InlineKeyboardButton(text_button_dynamics, callback_data='temp')
        markup_dynamics.add(dynamics_decision)
        bot.send_message(callback.message.chat.id, text_for_dynamic_supervision,
                         parse_mode='HTML', reply_markup=markup_dynamics)


# Постоянная работа бота.
bot.infinity_polling()
