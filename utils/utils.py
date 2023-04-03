import json
import pathlib


def path(file):
    """
    Прописывает путь до файла
    :param file: Имя файла
    :return: Абсолютный путь
    """
    dir_path = pathlib.Path.cwd()
    full_path = pathlib.Path(dir_path, "operation_files", file)
    return full_path


def load_json_file(filename):
    """
    Читает и конвертирует json файл
    :param filename: имя файла
    :return: конвертированный файл (список словарей)
    """
    with open(path(filename), "r", encoding="utf8") as json_file:
        converted_file = json.load(json_file)
        return converted_file


if __name__ == '__main__':
    print(load_json_file("operations.json"))
    print(path("operations.json"))
