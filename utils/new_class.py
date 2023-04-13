from datetime import date, datetime, time


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

    def __init__(self, operation_id=None, operation_date=None, state=None, amount=None, currency=None, description=None,
                 from_where=None, to=None):
        self.operation_id = operation_id
        self.operation_date = operation_date
        self.state = state
        self.amount = amount
        self.currency = currency
        self.description = description
        self.from_where = from_where
        self.to = to

    def __repr__(self):
        """
        :return: Operation(date = {self.operation_date}, state = {self.state}, amount = {self.amount},
        description = {self.description}, from_where = {self.from_where}, to = {self.to}, currency = {self.currency})
        """
        return f"Operation(date = {self.operation_date}, " \
               f"state = {self.state}, " \
               f"amount = {self.amount}, " \
               f"description = {self.description}, " \
               f"from_where = {self.from_where}, " \
               f"to = {self.to}, " \
               f"currency = {self.currency}"

    def get_id(self):
        """
        Возвращает id операции экземпляра класса Operation
        :return: str
        """
        return self.operation_id

    def get_date(self):
        """
        Возвращает дату операции экземпляра класса Operation
        :return: str
        """
        return self.operation_date

    def get_state(self):
        """
        Возвращает статус операции экземпляра класса Operation
        :return: str
        """
        return self.state

    def get_amount(self):
        """
        Возвращает сумму операции экземпляра класса Operation
        :return: str
        """
        return self.amount

    def get_description(self):
        """
        Возвращает описание операции экземпляра класса Operation
        :return: str
        """
        return self.description

    def get_from_where(self):
        """
        Возвращает отправителя операции экземпляра класса Operation
        :return: str
        """
        return self.from_where

    def get_to(self):
        """
        Возвращает получателя операции экземпляра класса Operation
        :return: str
        """
        return self.to

    def get_currency(self):
        """
        Возвращает валюту операции экземпляра класса Operation
        :return: str
        """
        return self.currency

    def convert_date(self):
        """
        Конвертирует дату из полученного формата в формат "%d.%m.%Y"
        :return: "%d.%m.%Y"
        """
        date_list = self.get_date().split("T")
        new_date = date.fromisoformat(date_list[0])
        date_formatted = new_date.strftime("%d.%m.%Y")
        return date_formatted

    def take_date_not_str(self):
        """
        Конвертирует дату в формат даты datetime
        :return: datetime
        """
        date_list = self.get_date().split("T")
        new_date = date_list[0]
        new_time = date_list[1]
        date_and_time = new_date + " " + new_time
        new_date_and_time = datetime.fromisoformat(date_and_time)
        return new_date_and_time

    def cypher_from(self):
        """
        Шифрует номер счёта или карты отправителя
        :return:
        """
        card_number_list = self.get_from_where().split(" ")
        if "Счет" in card_number_list[0]:
            return self.cypher_account_number(card_number_list)
        else:
            return self.cypher_card_number(card_number_list)

    def cypher_to(self):
        """
        Шифрует номер счёта или карты получателя
        :return:
        """
        account_number_list = self.get_to().split(" ")
        if "Счет" in account_number_list[0]:
            return self.cypher_account_number(account_number_list)
        else:
            return self.cypher_card_number(account_number_list)

    def cypher_card_number(self, card_number_list):
        """
        Шифрует номер счёта
        :param card_number_list: ["Visa", "1231231231231231"]
        :return: Visa 1231 23** **** 1231
        """
        try:
            raw_card_number = card_number_list[2]
            new_raw_card_number = [raw_card_number[0:6], raw_card_number[6:12], raw_card_number[12:]]
            formatting_list = [new_raw_card_number[0]]
            for digit in new_raw_card_number[1]:
                cyphered_digit = digit.replace(digit, "*")
                formatting_list.append(cyphered_digit)
            formatting_list.append(new_raw_card_number[2])
            cyphered_card_number = "".join(formatting_list)
            return card_number_list[0] + " " + card_number_list[1] + " " + " ".join(
                [cyphered_card_number[i:i + 4] for i in range(0, len(cyphered_card_number), 4)])
        except IndexError:
            raw_card_number = card_number_list[1]
            new_raw_card_number = [raw_card_number[0:6], raw_card_number[6:12], raw_card_number[12:]]
            formatting_list = [new_raw_card_number[0]]
            for digit in new_raw_card_number[1]:
                cyphered_digit = digit.replace(digit, "*")
                formatting_list.append(cyphered_digit)
            formatting_list.append(new_raw_card_number[2])
            cyphered_card_number = "".join(formatting_list)
            return card_number_list[0] + " " + " ".join(
                [cyphered_card_number[i:i + 4] for i in range(0, len(cyphered_card_number), 4)])

    def cypher_account_number(self, account_number_list):
        """
        Шифрует номер счёта
        :param account_number_list: ["Счет", "1231231231231231"]
        :return: Счет **1231
        """
        raw_card_number = account_number_list[1]
        account_number_tail = raw_card_number[-6:]
        account_number_tail_list = [account_number_tail[:2], account_number_tail[2:]]
        visible_list = []
        for digit in account_number_tail_list[0]:
            cyphered_digit = digit.replace(digit, "*")
            visible_list.append(cyphered_digit)
        visible_list.append(account_number_tail_list[1])
        return account_number_list[0] + " " + "".join(visible_list)
