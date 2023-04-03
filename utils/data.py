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

    def __init__(self, operation_date=None, state=None, amount=None, description=None, from_where=None, to=None):
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

    def cypher_card_number(self):
        card_number_list = self.get_from_where().split(" ")
        raw_card_number = card_number_list[1]
        new_raw_card_number = [raw_card_number[0:6], raw_card_number[6:12], raw_card_number[12:]]
        formatting_list = [new_raw_card_number[0]]
        for digit in new_raw_card_number[1]:
            cyphered_digit = digit.replace(digit, "*")
            formatting_list.append(cyphered_digit)
        formatting_list.append(new_raw_card_number[2])
        cyphered_card_number = "".join(formatting_list)
        return " ".join([cyphered_card_number[i:i+4] for i in range(0, len(cyphered_card_number), 4)])

    def cypher_account_number(self):
        raw_account_number = self.get_to().split(" ")[1]
        account_number_tail = raw_account_number[-6:]
        account_number_tail_list = [account_number_tail[:2], account_number_tail[2:]]
        visible_list = []
        for digit in account_number_tail_list[0]:
            cyphered_digit = digit.replace(digit, "*")
            visible_list.append(cyphered_digit)
        visible_list.append(account_number_tail_list[1])
        return "".join(visible_list)



if __name__ == '__main__':
    qqq = Operation()
    qqq.to = "Счет 64686473678894779589"
    print(qqq.cypher_account_number())

