from src.item import Item


class MixinKeyboard:
    def __init__(self, language='EN'):
        self.__language = language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'



class Keyboard(Item, MixinKeyboard):
    pass
