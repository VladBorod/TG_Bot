from text_for_user import *

body_weight = float(1.5)


def sultasini_calculation(weight):
    """Функция расчета сультасина"""
    global body_weight
    result = body_weight * 75
    return result, text_sultasini_message


sul = sultasini_calculation(body_weight)
