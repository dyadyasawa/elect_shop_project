from src.item import Item


class MixinKeyboard:
    """ Класс-миксин для “подмешивания” в цепочку наследования класса `Keyboard` """
    def __init__(self, language='EN'):
        self.__language = language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        raise AttributeError('Язык менять нельзя!')


class Keyboard(Item, MixinKeyboard):
    """ Класс Keyboard для товара “клавиатура” """
    pass
