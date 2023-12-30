
from src.keyboard import Keyboard

kb1 = Keyboard('Обычная клавиатура', 2200, 8)


def test_language():
    """ Тест для атрибута language """
    assert str(kb1) == 'Обычная клавиатура'
    assert str(kb1.language) == 'EN'


def test_change_lang():
    """ Тест метода change_lang """
    kb1.change_lang()
    assert str(kb1.language) == "RU"

    kb1.change_lang()
    assert str(kb1.language) == "EN"
