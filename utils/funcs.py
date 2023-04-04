import json
import pathlib
from utils.new_class import Operation


def path(file):
    """
    Прописывает путь до файла
    :param file: Имя файла
    :return: Абсолютный путь
    """
    dir_path = pathlib.Path.cwd()
    full_path = pathlib.Path(dir_path, "operation_files", file)
    return full_path


def load_json_file():
    """
    Читает и конвертирует json файл
    :param filename: имя файла
    :return: конвертированный файл (список словарей)
    """
    with open(path("operations.json"), "r", encoding="utf8") as json_file:
        converted_file = json.load(json_file)
        return converted_file


def load_operation():
    new_operation = None
    for operation in load_json_file():
        try:
            new_operation = Operation(operation_id=operation["id"], operation_date = operation["date"], state=operation["state"],
                                      amount=operation["operationAmount"]["amount"],
                                      currency=operation["operationAmount"]["currency"]["name"],
                                      description=operation["description"], from_where=operation["from"], to=operation["to"])
        except KeyError:
            continue
        if operation != new_operation:
            break

    return new_operation


if __name__ == '__main__':
    print(load_operation())
