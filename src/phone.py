from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim: int):
        super().__init__(name, price, quantity)
        if number_of_sim <= 0:
            raise ValueError('Количество sim-карт должно быть больше нуля')
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        return int(self.quantity) + int(other.quantity)
