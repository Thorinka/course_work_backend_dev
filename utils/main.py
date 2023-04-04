from utils.funcs import load_operation, load_json_file
from utils.new_class import Operation
import heapq


def main():
    executed_operations = []
    for operation in load_json_file():
        try:
            new_operation = Operation(operation_id=operation["id"], operation_date=operation["date"],
                                  state=operation["state"],
                                  amount=operation["operationAmount"]["amount"],
                                  currency=operation["operationAmount"]["currency"]["name"],
                                  description=operation["description"], from_where=operation["from"],
                                  to=operation["to"])
        except:
            continue
        if new_operation.get_state() == "EXECUTED":
            executed_operations.append(new_operation)
    last_executed_operations_dates = heapq.nlargest(5, [i.take_date_not_str() for i in executed_operations])
    last_executed_operations = []
    for i in executed_operations:
        if i.take_date_not_str() in last_executed_operations_dates:
            last_executed_operations.append(i)


    return print(last_executed_operations)


if __name__ == '__main__':
    main()
