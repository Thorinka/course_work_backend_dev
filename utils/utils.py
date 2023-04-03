import json
import pathlib


def path(file):
    dir_path = pathlib.Path.cwd()
    full_path = pathlib.Path(dir_path, "operation_files", file)
    return full_path


def load_json_file(filename):
    with open(path(filename), "r", encoding="utf8") as json_file:
        converted_file = json.load(json_file)
        return converted_file


if __name__ == '__main__':
    print(load_json_file("operations.json"))
    print(path("operations.json"))
