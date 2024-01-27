from src.item import Item
from tests.test_config import NONEXIST_FILE_PATH, DAMAGED_FILE_PATH


if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(NONEXIST_FILE_PATH)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(DAMAGED_FILE_PATH)
    # InstantiateCSVError: Файл item.csv поврежден
