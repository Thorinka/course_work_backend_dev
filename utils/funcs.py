import json
import os
import pathlib
from utils.new_class import Operation


PATH_TO_FILE = os.path.join("..", "operation_files", "operations.json")


def load_json_file(filename):
    """
    Читает и конвертирует json файл
    :param filename: имя файла
    :return: конвертированный файл (список словарей)
    """
    with open(PATH_TO_FILE, "r", encoding="utf8") as json_file:
        converted_file = json.load(json_file)
        return converted_file


def load_operation(operation):
    new_operation = Operation()
    try:
        new_operation.set_id(operation["id"])
    except KeyError:
        new_operation.set_id(None)
    try:
        new_operation.set_date(operation["date"])
    except KeyError:
        new_operation.set_date(None)
    try:
        new_operation.set_state(operation["state"])
    except KeyError:
        new_operation.set_state(None)
    try:
        new_operation.set_amount(operation["operationAmount"]["amount"])
    except KeyError:
        new_operation.set_amount(None)
    try:
        new_operation.set_currency(operation["operationAmount"]["currency"]["name"])
    except KeyError:
        new_operation.set_currency(None)
    try:
        new_operation.set_description(operation["description"])
    except KeyError:
        new_operation.set_description(None)
    try:
        new_operation.set_from_where(operation["from"])
    except KeyError:
        new_operation.set_from_where(None)
    try:
        new_operation.set_to(operation["to"])
    except KeyError:
        new_operation.set_to(None)
    return new_operation


if __name__ == '__main__':
    for operation in load_json_file("operations.json"):
        print(load_operation(operation))
