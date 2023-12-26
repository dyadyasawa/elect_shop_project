from csv import DictReader

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)


    def __str__(self):
        return self.__name


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        return int(self.quantity) + int(other.quantity)


    @property
    def name(self):
        return self.__name[0:10]

    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity * Item.pay_rate

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        """класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv"""

        cls.all.clear()
        with open(csv_file, newline='', encoding='windows-1251') as f:
            reader = DictReader(f)
            for row in reader:
                Item(name=row['name'], price=float(row['price']), quantity=int(row['quantity']))

    @staticmethod
    def string_to_number(str_num):
        """статический метод, возвращающий число из числа-строки"""

        return int(float(str_num))



