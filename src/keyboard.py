from src.item import Item


class LanguageMixin:
    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language not in {'EN', 'RU'}:
            raise AttributeError("AttributeError: property 'language' of 'Keyboard' object has no setter")
        self._language = 'RU' if self._language == 'EN' else 'EN'


class Keyboard(Item, LanguageMixin):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)

    def __str__(self):
        return super().__str__()
