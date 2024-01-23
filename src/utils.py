import json
from config import *
import re
from datetime import datetime


def load_json():
    """
    загрузка файла operations.json
    """
    with open(OPERATION, 'r', encoding="UTF-8") as file:
        json_user_operations = json.load(file)
    return json_user_operations


def get_exeсs(values):
    """
    Сортировка operations.json
    """
    execs_operations = []
    for value in values:
        if value == {}:
            continue
        elif value['state'] == 'EXECUTED':
            execs_operations.append(value)
    return execs_operations


def sort_dates(operations):
    """
    Вывод последних пяти операций
    """
    sorted_list = sorted(operations, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    listed_values = sorted_list[:5]
    return listed_values


def date_format(date):
    """
    Форматирование даты
    """
    date_operations = []
    for listed_data in date:
        sorted_data = datetime.strptime(listed_data['date'], "%Y-%m-%dT%H:%M:%S.%f")
        formated_date = f"{sorted_data:%d.%m.%Y}"
        date_operations.append(formated_date)
    return date_operations


def hide_card_number(card_numbers):
    """
    скрытие номера карты
    """
    card_number_operations = []
    for card_number in card_numbers:
        if card_number['description'] == "Открытие вклада":
            card_number['from'] = f"Счёт клиента: {card_number['to'][5:]}"
        mask_card = card_number['from'].split()
        mask_card_copy = mask_card.copy()
        del mask_card_copy[-1]
        card_mask = re.findall('....', mask_card[-1])
        number_card = card_mask[0], card_mask[1][0:2] + '**', card_mask[2].replace(card_mask[2], '****'), card_mask[3:]
        mask_number = " ".join(number_card[3])
        card_number_operations.append(f"{' '.join(mask_card_copy)} {' '.join(list(number_card[0:3]))} {mask_number}")
    return card_number_operations


def hide_amount_number(amount_numbers):
    """
    скрытие номера счета
    """
    amount_number_operations = []
    for amount_number in amount_numbers:
        format_to_check = re.findall('....', amount_number['to'])
        check_to_format = format_to_check[4:]
        number_amount = check_to_format[0].replace(check_to_format[0], '**'), check_to_format[1]
        amount_mask = ''.join(list(number_amount))
        amount_number_operations.append(amount_mask)
    return amount_number_operations
