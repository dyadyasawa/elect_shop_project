"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

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