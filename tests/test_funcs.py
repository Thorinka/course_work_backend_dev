import os
from pathlib import WindowsPath

from utils.funcs import load_json_file
import pytest

PATH_TO_FILE = os.path.join('..', 'utils', 'operation_file')

def test_load_json_file():
    assert isinstance(load_json_file(PATH_TO_FILE), list) == True

