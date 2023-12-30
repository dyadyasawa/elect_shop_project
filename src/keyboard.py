from src.item import Item


class MixinKeyboard:
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
    pass
