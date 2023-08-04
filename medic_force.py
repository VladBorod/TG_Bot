import telebot
from telebot import types

from text_for_user import *
from bot_token import bot_token
from choose_func import *

bot = telebot.TeleBot(bot_token)


# Стартовое меню.
@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name is not None:
        bot.send_message(message.chat.id, f'<b>Приветствую {message.from_user.first_name} '
                                          f'{message.from_user.last_name}. Я молодой и начинающий свой путь робот,'
                                          f'созданный для помощи и подсказок куда более разумной особи чем я. </b>'
                                          f'<b><u>А потому прошу тебя быть внимательным в своем выборе! </u></b>'
                                          f'<b>Начните с нажатия кнопки Menu в левом нижнем углу.</b>',
                         parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, f'<b>Приветствую {message.from_user.first_name}. '
                                          f'Я молодой и начинающий свой путь робот,'
                                          f'созданный для помощи и подсказок куда более разумной особи чем я. </b>'
                                          f'<b><u>А потому прошу тебя быть внимательным в своем выборе! </u></b>'
                                          f'<b>Начните с нажатия кнопки Menu в левом нижнем углу.</b>',
                         parse_mode='HTML')


@bot.message_handler(commands=['antibiotics'])
def antibiotics(message):
    """"Это стартовый метод!"""
    # Приветствие с пользователем.
    if message.from_user.last_name is not None:
        bot.send_message(message.chat.id, f'<b>{message.from_user.first_name} {message.from_user.last_name}, '
                                          f'давайте рассчитаем антибиотики! </b>',
                         parse_mode='html')
    else:
        bot.send_message(message.chat.id, f'<b>{message.from_user.first_name}, '
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
def antibiotics_algorithm(callback):
    """Работа с антибиотиками!"""
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
        # Варианты ГВ и ПКВ!
        markup_amikacini_fork_f_gestage.add(gesage_35_more,
                                            gesage_30_34_postcon_0,
                                            gesage_30_34_postcon_8,
                                            gesage_less_29_postcon_0_7,
                                            gesage_less_29_postcon_8_28,
                                            gesage_less_29_postcon_29,
                                            go_to_second_antibiotic_in_combotherapy)
        bot.send_message(callback.message.chat.id, text_for_gestational_age,
                         parse_mode='HTML', reply_markup=markup_amikacini_fork_f_gestage)
    # Разные тексты КРАТНОСТИ на разные ГВ и ПКВ.
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
    # Второй антибиотик.
    elif callback.data == 'second_antibiotic_in_combitherapy':
        markup_second_antibiotic_combitherapy = types.InlineKeyboardMarkup(row_width=1)
        # Кнопка дополнительной терапии Сультасином.
        go_to_prescribe_sultas_combi = types.InlineKeyboardButton(text_button_to_prescribe_monotherapy_sultas,
                                                                 callback_data='prescribe_combi_therapy_sultas')
        # Кнопка дополнительной терапии Ампициллином.
        go_to_prescribe_ampi_combi = types.InlineKeyboardButton(text_button_to_prescribe_monotherapy_ampi,
                                                                        callback_data='prescribe_combi_therapy_ampi')
        markup_second_antibiotic_combitherapy.add(go_to_prescribe_sultas_combi, go_to_prescribe_ampi_combi)
        bot.send_message(callback.message.chat.id, text_for_prescribing_combi_antibiotic,
                         parse_mode='HTML', reply_markup=markup_second_antibiotic_combitherapy)
    # Переход к методу для назначения вторым Сультасином!
    elif callback.data == 'prescribe_combi_therapy_sultas':
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
        bot.register_next_step_handler(callback.message, sultasini_calculation)
    # Переход к методу для назначения вторым Ампициллином!
    elif callback.data == 'prescribe_combi_therapy_ampi':
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
        bot.register_next_step_handler(callback.message, ampicillini_calculation)
    # СМЕНА АНТИБАКТЕРИАЛКИ!!!
    elif callback.data == 'antibiotics_change':
        markup_antibio_change = types.InlineKeyboardMarkup(row_width=2)
        bot.send_message(callback.message.chat.id, text_for_long_short_antib_therapy, parse_mode='HTML')
        sympt_for_long_therapy_yes = types.InlineKeyboardButton(text_button_deterioration_yes,
                                                                callback_data='deterioration_yes')
        sympt_for_long_therapy_no = types.InlineKeyboardButton(text_button_deterioration_no,
                                                               callback_data='deterioration_no')
        markup_antibio_change.add(sympt_for_long_therapy_yes, sympt_for_long_therapy_no)
        bot.send_message(callback.message.chat.id, text_ask_y_n_sympths, parse_mode='HTML',
                         reply_markup=markup_antibio_change)
    # Нет симптомов + сообщение о вариантах отмены.
    elif callback.data == 'deterioration_no':
        bot.send_message(callback.message.chat.id, text_to_abort_antibio, parse_mode='HTML')
    # Симптомы есть, идем к смене АБТ.
    elif callback.data == 'deterioration_yes':
        markup_antibio_deterior_yes = types.InlineKeyboardMarkup(row_width=1)
        go_to_prescribe_amikacini = types.InlineKeyboardButton(text_button_to_prescribe_amikacini,
                                                               callback_data='prescribe_amikacini')
        antibio_change = types.InlineKeyboardButton(text_deterioraton_change, callback_data='antibio_change')
        markup_antibio_deterior_yes.add(go_to_prescribe_amikacini, antibio_change)
        bot.send_message(callback.message.chat.id, text_to_prolong_antibio, parse_mode='HTML',
                         reply_markup=markup_antibio_deterior_yes)
    # Назначаем МЕРОНЕМ!!!
    elif callback.data == 'antibio_change':
        markup_ilness_conditions = types.InlineKeyboardMarkup(row_width=1)
        mening_and_dessim_infect = types.InlineKeyboardButton(text_mening_and_dessim_infect,
                                                              callback_data='mening_dessim_infect')
        mening_ruled_out = types.InlineKeyboardButton(text_mening_ruled_out,
                                                      callback_data='mening_r_o')
        intraabd_non_cns_infect = types.InlineKeyboardButton(text_f_intraabdom_non_cns_inf,
                                                             callback_data='intraabd_non_cns')
        mening_bacterial = types.InlineKeyboardButton(text_f_bacterial_meningitis,
                                                      callback_data='bact_mening')
        markup_ilness_conditions.add(mening_and_dessim_infect, mening_ruled_out, intraabd_non_cns_infect,
                                     mening_bacterial)
        bot.send_message(callback.message.chat.id, text_to_choose_ilness_abt_change,
                         parse_mode='HTML', reply_markup=markup_ilness_conditions)
    elif callback.data == 'mening_dessim_infect':
        markup_mening_dessim_infect = types.InlineKeyboardMarkup(row_width=1)
        from_32_gw_0_7 = types.InlineKeyboardButton(text_from_32_gw_0_7, callback_data='20_8_meron')
        from_32_gw_7_30 = types.InlineKeyboardButton(text_from_32_gw_7_30, callback_data='30_8_meron')
        add_fluconazoli = types.InlineKeyboardButton(text_add_fluconazoli, callback_data='add_fluconaz')
        markup_mening_dessim_infect.add(from_32_gw_0_7, from_32_gw_7_30, add_fluconazoli)
        bot.send_message(callback.message.chat.id, text_to_choose_gw_in_mero, parse_mode='HTML',
                         reply_markup=markup_mening_dessim_infect)
    elif callback.data == 'mening_r_o':
        markup_mening_r_o = types.InlineKeyboardMarkup(row_width=1)
        from_32_to_34_0_7 = types.InlineKeyboardButton(text_from_32_to_34_0_7, callback_data='13_8_meron')
        from_32_to_34_7_30 = types.InlineKeyboardButton(text_from_32_to_34_7_30, callback_data='20_8_meron')
        from_34_0_30 = types.InlineKeyboardButton(text_from_34_0_30, callback_data='20_8_meron')
        add_fluconazoli = types.InlineKeyboardButton(text_add_fluconazoli, callback_data='add_fluconaz')
        markup_mening_r_o.add(from_32_to_34_0_7, from_32_to_34_7_30, from_34_0_30, add_fluconazoli)
        bot.send_message(callback.message.chat.id, text_to_choose_gw_in_mero, parse_mode='HTML',
                         reply_markup=markup_mening_r_o)
    elif callback.data == 'intraabd_non_cns':
        intraabdom_non_cns = types.InlineKeyboardMarkup(row_width=1)
        less_32_pca_less_14 = types.InlineKeyboardButton(text_less_32_pca_less_14, callback_data='20_12_meron')
        less_32_pca_more_14 = types.InlineKeyboardButton(text_less_32_pca_more_14, callback_data='20_8_meron')
        more_32_pca_less_14 = types.InlineKeyboardButton(text_more_32_pca_less_14, callback_data='20_8_meron')
        more_32_pca_more_14 = types.InlineKeyboardButton(text_more_32_pca_more_14, callback_data='30_8_meron')
        add_fluconazoli = types.InlineKeyboardButton(text_add_fluconazoli, callback_data='add_fluconaz')
        intraabdom_non_cns.add(less_32_pca_less_14, less_32_pca_more_14, more_32_pca_less_14, more_32_pca_more_14,
                               add_fluconazoli)
        bot.send_message(callback.message.chat.id, text_to_choose_gw_in_mero, parse_mode='HTML',
                         reply_markup=intraabdom_non_cns)
    elif callback.data == 'bact_mening':
        bacterial_mening = types.InlineKeyboardMarkup(row_width=1)
        less_32_w_pca_less_14 = types.InlineKeyboardButton(text_less_32_w_pca_less_14, callback_data='40_8_meron')
        less_32_w_pca_more_14 = types.InlineKeyboardButton(text_less_32_w_pca_more_14, callback_data='40_8_meron')
        more_32_w_pca_no_matters = types.InlineKeyboardButton(text_more_32_w_pca_no_matters, callback_data='40_8_meron')
        add_fluconazoli = types.InlineKeyboardButton(text_add_fluconazoli, callback_data='add_fluconaz')
        bacterial_mening.add(less_32_w_pca_less_14, less_32_w_pca_more_14, more_32_w_pca_no_matters, add_fluconazoli)
        bot.send_message(callback.message.chat.id, text_to_choose_gw_in_mero, parse_mode='HTML',
                         reply_markup=bacterial_mening)
    elif callback.data == '13_8_meron':
        bot.register_next_step_handler(callback.message, meronemi_calculation_13)
        bot.send_message(callback.message.chat.id, text_f_meronemi_13_8, parse_mode='HTML')
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
    elif callback.data == '20_8_meron':
        bot.register_next_step_handler(callback.message, meronemi_calculation_20)
        bot.send_message(callback.message.chat.id, text_f_meronemi_20_8, parse_mode='HTML')
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
    elif callback.data == '20_12_meron':
        bot.register_next_step_handler(callback.message, meronemi_calculation_20)
        bot.send_message(callback.message.chat.id, text_f_meronemi_20_12, parse_mode='HTML')
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
    elif callback.data == '30_8_meron':
        bot.register_next_step_handler(callback.message, meronemi_calculation_30)
        bot.send_message(callback.message.chat.id, text_f_meronemi_30_8, parse_mode='HTML')
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
    elif callback.data == '40_8_meron':
        bot.register_next_step_handler(callback.message, meronemi_calculation_40)
        bot.send_message(callback.message.chat.id, text_f_meronemi_40_8, parse_mode='HTML')
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
    elif callback.data == 'add_fluconaz':
        fluconazoli_g_w = types.InlineKeyboardMarkup(row_width=1)
        add_flucon_29_6_pca_less_14 = types.InlineKeyboardButton(text_add_flucon_29_6_less_14,
                                                                 callback_data='flucon_multi_72')
        add_flucon_30_36_6_pca_less_14 = types.InlineKeyboardButton(text_add_flucon_30_36_6_less_14,
                                                                    callback_data='flucon_multi_48')
        add_flucon_37_more_pca = types.InlineKeyboardButton(text_add_flucon_37_more,
                                                                    callback_data='flucon_multi_24')
        add_flucon_29_6_pca_more_14 = types.InlineKeyboardButton(text_add_flucon_29_6_more_14,
                                                                 callback_data='flucon_multi_48')
        add_flucon_30_36_6_pca_more_14 = types.InlineKeyboardButton(text_add_flucon_30_36_6_more_14,
                                                                    callback_data='flucon_multi_24')
        add_vancomycini = types.InlineKeyboardButton(text_bt_add_vancomycini,
                                                     callback_data='add_vancomycini')
        fluconazoli_g_w.add(add_flucon_29_6_pca_less_14, add_flucon_30_36_6_pca_less_14, add_flucon_29_6_pca_more_14,
                            add_flucon_30_36_6_pca_more_14, add_flucon_37_more_pca, add_vancomycini)
        bot.send_message(callback.message.chat.id, text_to_choose_gw_in_mero, parse_mode='HTML',
                         reply_markup=fluconazoli_g_w)
    elif callback.data == 'flucon_multi_72':
        bot.register_next_step_handler(callback.message, fluconazoli_calculation_40)
        bot.send_message(callback.message.chat.id, text_f_fluconazoli_72, parse_mode='HTML')
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
    elif callback.data == 'flucon_multi_48':
        bot.register_next_step_handler(callback.message, fluconazoli_calculation_40)
        bot.send_message(callback.message.chat.id, text_f_fluconazoli_48, parse_mode='HTML')
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
    elif callback.data == 'flucon_multi_24':
        bot.register_next_step_handler(callback.message, fluconazoli_calculation_40)
        bot.send_message(callback.message.chat.id, text_f_fluconazoli_24, parse_mode='HTML')
        bot.send_message(callback.message.chat.id, text_for_weight_input, parse_mode='HTML')
    elif callback.data == 'add_vancomycini':
        markup_vanco_add = types.InlineKeyboardMarkup(row_width=1)
        add_vanco_less_29_w_0_14 = types.InlineKeyboardButton(text_add_vanco_less_29_w_0_14,
                                                              callback_data='29_0_14_vanco')
        add_vanco_less_29_w_14_more = types.InlineKeyboardButton(text_add_vanco_less_29_w_14_more,
                                                                 callback_data='29_14_m_vanco')
        add_vanco_30_36_w_0_14 = types.InlineKeyboardButton(text_add_vanco_30_36_w_0_14,
                                                            callback_data='30_36_14_vanco')
        add_vanco_30_36_w_14_more = types.InlineKeyboardButton(text_add_vanco_30_36_w_14_more,
                                                               callback_data='30_36_14_m_vanco')
        add_vanco_37_44_w_0_7 = types.InlineKeyboardButton(text_add_vanco_37_44_w_0_7,
                                                           callback_data='37_44_7_vanco')
        add_vanco_37_44_w_7_more = types.InlineKeyboardButton(text_add_vanco_37_44_w_7_more,
                                                              callback_data='37_44_7_m_vanco')
        add_vanco_45_w_more = types.InlineKeyboardButton(text_add_vanco_45_w_more,
                                                         callback_data='45_m_vanco')
        add_vanco_creatinin_monitoring = types.InlineKeyboardButton(text_add_vanco_creatinin_monitoring,
                                                                    callback_data='creat_elevation_vanco')
        markup_vanco_add.add(add_vanco_less_29_w_0_14, add_vanco_less_29_w_14_more, add_vanco_30_36_w_0_14,
                             add_vanco_30_36_w_14_more, add_vanco_37_44_w_0_7, add_vanco_37_44_w_7_more,
                             add_vanco_45_w_more, add_vanco_creatinin_monitoring)
        bot.send_message(callback.message.chat.id, text_before_vanco_forks, parse_mode='HTML')
        bot.send_message(callback.message.chat.id, text_for_pma_or_ser_creat, parse_mode='HTML',
                         reply_markup=markup_vanco_add)
    elif callback.data == '29_0_14_vanco':
        markup_vanco_29_0_14 = types.InlineKeyboardMarkup(row_width=2)
        choice_10_mg = types.InlineKeyboardButton(text_choice_10_mg, callback_data='vanco_10_mg_18h')
        choice_15_mg = types.InlineKeyboardButton(text_choice_15_mg, callback_data='vanco_15_mg_18h')
        # choice_20_mg = types.InlineKeyboardButton(text_choice_20_mg, callback_data='vanco_20_mg_18h')
        markup_vanco_29_0_14.add(choice_10_mg, choice_15_mg)
        bot.send_message(callback.message.chat.id, text_choose_dose_vanco, parse_mode='HTML',
                         reply_markup=markup_vanco_29_0_14)
    elif callback.data == '29_14_m_vanco':
        markup_vanco_29_14_m = types.InlineKeyboardMarkup(row_width=2)
        choice_10_mg = types.InlineKeyboardButton(text_choice_10_mg, callback_data='vanco_10_mg_12h')
        choice_15_mg = types.InlineKeyboardButton(text_choice_15_mg, callback_data='vanco_15_mg_12h')
        # choice_20_mg = types.InlineKeyboardButton(text_choice_20_mg, callback_data='vanco_20_mg_12h')
        markup_vanco_29_14_m.add(choice_10_mg, choice_15_mg)
        bot.send_message(callback.message.chat.id, text_choose_dose_vanco, parse_mode='HTML',
                         reply_markup=markup_vanco_29_14_m)
    elif callback.data == '30_36_14_vanco':
        markup_vanco_30_36_0_14 = types.InlineKeyboardMarkup(row_width=2)
        choice_10_mg = types.InlineKeyboardButton(text_choice_10_mg, callback_data='vanco_10_mg_12h')
        choice_15_mg = types.InlineKeyboardButton(text_choice_15_mg, callback_data='vanco_15_mg_12h')
        # choice_20_mg = types.InlineKeyboardButton(text_choice_20_mg, callback_data='vanco_20_mg_12h')
        markup_vanco_30_36_0_14.add(choice_10_mg, choice_15_mg)
        bot.send_message(callback.message.chat.id, text_choose_dose_vanco, parse_mode='HTML',
                         reply_markup=markup_vanco_30_36_0_14)
    elif callback.data == '30_36_14_m_vanco':
        markup_vanco_30_36_14_m = types.InlineKeyboardMarkup(row_width=2)
        choice_10_mg = types.InlineKeyboardButton(text_choice_10_mg, callback_data='vanco_10_mg_8h')
        choice_15_mg = types.InlineKeyboardButton(text_choice_15_mg, callback_data='vanco_15_mg_8h')
        # choice_20_mg = types.InlineKeyboardButton(text_choice_20_mg, callback_data='vanco_20_mg_8h')
        markup_vanco_30_36_14_m.add(choice_10_mg, choice_15_mg)
        bot.send_message(callback.message.chat.id, text_choose_dose_vanco, parse_mode='HTML',
                         reply_markup=markup_vanco_30_36_14_m)
    elif callback.data == '37_44_7_vanco':
        markup_vanco_37_44_0_14 = types.InlineKeyboardMarkup(row_width=2)
        choice_10_mg = types.InlineKeyboardButton(text_choice_10_mg, callback_data='vanco_10_mg_12h')
        choice_15_mg = types.InlineKeyboardButton(text_choice_15_mg, callback_data='vanco_15_mg_12h')
        # choice_20_mg = types.InlineKeyboardButton(text_choice_20_mg, callback_data='vanco_20_mg_12h')
        markup_vanco_37_44_0_14.add(choice_10_mg, choice_15_mg)
        bot.send_message(callback.message.chat.id, text_choose_dose_vanco, parse_mode='HTML',
                         reply_markup=markup_vanco_37_44_0_14)
    elif callback.data == '37_44_7_m_vanco':
        markup_vanco_37_44_14_m = types.InlineKeyboardMarkup(row_width=2)
        choice_10_mg = types.InlineKeyboardButton(text_choice_10_mg, callback_data='vanco_10_mg_8h')
        choice_15_mg = types.InlineKeyboardButton(text_choice_15_mg, callback_data='vanco_15_mg_8h')
        # choice_20_mg = types.InlineKeyboardButton(text_choice_20_mg, callback_data='vanco_20_mg_8h')
        markup_vanco_37_44_14_m.add(choice_10_mg, choice_15_mg)
        bot.send_message(callback.message.chat.id, text_choose_dose_vanco, parse_mode='HTML',
                         reply_markup=markup_vanco_37_44_14_m)
    elif callback.data == '45_m_vanco':
        markup_vanco_45_m = types.InlineKeyboardMarkup(row_width=2)
        choice_10_mg = types.InlineKeyboardButton(text_choice_10_mg, callback_data='vanco_10_mg_6')
        choice_15_mg = types.InlineKeyboardButton(text_choice_15_mg, callback_data='vanco_15_mg_6')
        # choice_20_mg = types.InlineKeyboardButton(text_choice_20_mg, callback_data='vanco_20_mg_12h')
        markup_vanco_45_m.add(choice_10_mg, choice_15_mg)
        bot.send_message(callback.message.chat.id, text_choose_dose_vanco, parse_mode='HTML',
                         reply_markup=markup_vanco_45_m)
    elif callback.data == 'creat_elevation_vanco':
        markup_vanco_creat_elevation = types.InlineKeyboardMarkup(row_width=1)
        creat_less_62 = types.InlineKeyboardButton(text_creat_less_62, callback_data='v_creat_less_62')
        creat_62_80 = types.InlineKeyboardButton(text_creat_62_80, callback_data='v_creat_62_80')
        creat_89_106 = types.InlineKeyboardButton(text_creat_89_106, callback_data='v_creat_89_106')
        creat_115_142 = types.InlineKeyboardButton(text_creat_115_142, callback_data='v_creat_115_142')
        creat_142_more = types.InlineKeyboardButton(text_creat_142_more, callback_data='v_creat_142_more')
        markup_vanco_creat_elevation.add(creat_less_62, creat_62_80, creat_89_106, creat_115_142, creat_142_more)
        bot.send_message(callback.message.chat.id, text_to_choose_creat_lvl, parse_mode='HTML',
                         reply_markup=markup_vanco_creat_elevation)



# Постоянная работа бота.
bot.infinity_polling()
