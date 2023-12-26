from src.phone import Phone
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_repr():
    """ Тест метода repr """
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add():
    """ Тест метода add """
    assert item1 + item1 == 40
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert phone1 + item1 == 25
