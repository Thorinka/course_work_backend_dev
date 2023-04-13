import datetime

from utils.new_class import Operation


def test_convert_date():
    test_object = Operation()
    test_object.operation_date = "2019-08-26T10:50:58.294041"
    assert test_object.convert_date() == "26.08.2019"

def test_take_date_not_str():
    test_object = Operation()
    test_object.operation_date = "2019-08-26T10:50:58.294041"
    assert test_object.take_date_not_str() == datetime.datetime(2019, 8, 26, 10, 50, 58, 294041)

def test_cypher_from():
    test_object = Operation()
    test_object.from_where = "Maestro 1596837868705199"
    assert test_object.cypher_from() == "Maestro 1596 83** **** 5199"

def test_cypher_to():
    test_object = Operation()
    test_object.to = "Счет 64686473678894779589"
    assert test_object.cypher_to() == "Счет **9589"

def test_cypher_card_number():
    test_object = Operation()
    card_number_list = ["Master", "Card", "1596837868705199"]
    assert test_object.cypher_card_number(card_number_list) == "Master Card 1596 83** **** 5199"

def test_cypher_account_number():
    test_object = Operation()
    account_number_list = ["Счет", "64686473678894779589"]
    assert test_object.cypher_account_number(account_number_list) == "Счет **9589"

def test_get_id():
    test_object = Operation()
    test_object.operation_id = "441945886"
    assert test_object.get_id() == "441945886"

def test_get_state():
    test_object = Operation()
    test_object.state = "EXECUTED"
    assert test_object.get_state() == "EXECUTED"

