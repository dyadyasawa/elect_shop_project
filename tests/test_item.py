"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.item import InstantiateCSVError
import pytest

product = Item('Телевизор', 30000, 5)
product_2 =Item('Холодильник', 55000, 2)
Item.pay_rate = 2.0


def test_calculate_total_price():
    """Тест функции calculate_total_price"""

    assert type(Item.calculate_total_price(product)) == float
    assert Item.calculate_total_price(product) == 300_000


def test_item_apply_discount():
    """Тест функции apply_discount"""

    Item.apply_discount(product)

    assert product.price == 60000


def test_len_name():
    """Тест формирования name с учетом заданной длины """

    assert product.name == 'Телевизор'
    assert product_2.name == 'Холодильни'


def test_instantiate_from_csv():
    """Тест метода instantiate_from_csv"""
    Item.all.clear()
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_instantiate_from_csv_file_not_found():
    """ Тест на возникновение исключения при отсутствии файла. """
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('it.csv')


def test_test_instantiate_from_csv_file_failed():
    """ Тест на возникновение исключения при поврежденном файле. """
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()


def test_string_to_number():
    """Тест метода string_to_number"""

    assert Item.string_to_number('6.8') == 6
    assert Item.string_to_number('11.0') == 11
    assert Item.string_to_number('53.1') == 53


def test_str():
    """Тест метода __str__"""

    assert str(product) == 'Телевизор'
    assert str(product_2) == 'Холодильник'


def test_repr():
    """Тест метода __repr__"""

    assert repr(product) == "Item('Телевизор', 60000.0, 5)"
    assert repr(product_2) == "Item('Холодильник', 55000, 2)"
