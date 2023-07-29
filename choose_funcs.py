from text_for_user import *

body_weight = float(0)


def sultasini_calculation(weight):
    """Функция расчета сультасина"""
    global body_weight
    result = body_weight * 75
    return result, sultasini_message
