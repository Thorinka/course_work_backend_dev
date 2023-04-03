from datetime import date


class Operation:
    """
    Класс - Операция
    Атрибуты: date - дата операции
    state - статус операции
    amount - сумма операции
    description - описание операции
    from_where - откуда совершена операция
    to - куда была совершена операция
    """
    def __init__(self, operation_date = None, state = None, amount = None, description = None, from_where = None, to = None):
        self.operation_date = operation_date
        self.state = state
        self.amount = amount
        self.description = description
        self.from_where = from_where
        self.to = to

    def __repr__(self):
        return f"Operation(date = {self.operation_date}, " \
               f"state = {self.state}, " \
               f"amount = {self.amount}, " \
               f"description = {self.description}, " \
               f"from_where = {self.from_where}, " \
               f"to = {self.to}"

    def get_date(self):
        return self.operation_date

    def get_state(self):
        return self.state

    def get_amount(self):
        return self.amount

    def get_description(self):
        return self.description

    def get_from_where(self):
        return self.from_where

    def get_to(self):
        return self.to

    def convert_date(self):
        date_list = self.get_date().split("T")
        new_date = date.fromisoformat(date_list[0])
        date_formatted = new_date.strftime("%d.%m.%Y")
        return date_formatted



if __name__ == '__main__':

