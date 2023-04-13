import json
import os

from utils.new_class import Operation

PATH_TO_FILE = os.path.join("..", "operation_files", "operations.json")


def load_json_file(filepath=PATH_TO_FILE):
    """
    Читает и конвертирует json файл
    :return: конвертированный файл (список словарей)
    """
    with open(filepath, "r", encoding="utf8") as json_file:
        converted_file = json.load(json_file)
        return converted_file


def load_operation(operation_):
    """
    Импортирует словарь из списка словарей в экземпляр класса Operation
    :param operation_: элемент списка словарей
    :return: Operation
    """
    try:
        new_operation = Operation(operation_date=operation_["date"], state=operation_["state"],
                                  amount=operation_["operationAmount"]["amount"],
                                  currency=operation_["operationAmount"]["currency"]["name"],
                                  description=operation_["description"], from_where=operation_["from"],
                                  to=operation_["to"])
    except:
        new_operation = Operation(operation_date=operation_["date"], state=operation_["state"],
                                  amount=operation_["operationAmount"]["amount"],
                                  currency=operation_["operationAmount"]["currency"]["name"],
                                  description=operation_["description"], from_where=None,
                                  to=operation_["to"])

    return new_operation
