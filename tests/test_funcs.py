import os

from utils.funcs import load_json_file, load_operation
from utils.new_class import Operation


PATH_TO_FILE = os.path.join("..", "operation_files", "operations.json")

def test_load_json_file():
    assert isinstance(load_json_file(PATH_TO_FILE), list) is True


def test_load_operation():
    for operation in load_json_file(PATH_TO_FILE):
        if operation:
            assert isinstance(load_operation(operation), Operation) == True

