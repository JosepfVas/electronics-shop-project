import csv


class InstantiateCSVError(Exception):
    pass


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.numbers = None
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        if len(name) > 10:
            self.__name = name[0:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price *= self.pay_rate

    @staticmethod
    def string_to_number(number):
        return int(float(number))

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        cls.all.clear()
        try:
            with open(csv_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise KeyError

                    name = str(row['name'])
                    price = int(row['price'])
                    quantity = int(row['quantity'])
                    cls(name, price, quantity)

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")
        except KeyError:
            raise InstantiateCSVError("Файл поврежден")

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.__name}", {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
