import os
from datetime import datetime
from utils.funcs import load_operation, load_json_file
import heapq

PATH_TO_FILE = os.path.join("operation_files", "operations.json")
def main():
    """
    Итерация по списку словарей из конвертированного файла JSON, фильтр по статусу EXECUTED, фильтр самых поздних
    операций, сортировка, вывод в зависимости от наличия элемента from_where

    :return: Возвращает форматированный список пяти последних выполненных операциях
    """
    executed_operations = []
    for operation in load_json_file(PATH_TO_FILE):
        if operation:
            new_operation = load_operation(operation)
            if new_operation.get_state() == "EXECUTED":
                executed_operations.append(new_operation)
    last_executed_operations_dates = heapq.nlargest(5, [i.take_date_not_str() for i in executed_operations])
    last_executed_operations = []
    for i in executed_operations:
        if i.take_date_not_str() in last_executed_operations_dates:
            last_executed_operations.append(i)
    sorted_list = sorted(
        last_executed_operations,
        key=lambda x: datetime.strptime(x.convert_date(), "%d.%m.%Y"), reverse=True)

    for i in sorted_list:
        if i.get_from_where() is not None:
            print(f"{i.convert_date()} {i.get_description()} \n"
                  f"{i.cypher_from()} -> {i.cypher_to()} \n"
                  f"{i.amount} {i.currency}\n")
        else:
            print(f"{i.convert_date()} {i.get_description()} \n"
                  f"{i.cypher_to()} \n"
                  f"{i.amount} {i.currency}\n")



if __name__ == '__main__':
    main()
