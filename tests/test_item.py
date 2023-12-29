from src.item import Item
import pytest


@pytest.fixture
def test_item():
    return Item(name="Test Item", price=10.0, quantity=2)
def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 20.0

def test_apply_discount(test_item):
    test_item.apply_discount()
    assert test_item.price == 10.0 * test_item.pay_rate
def test_all_items_list(test_item):
    assert test_item in Item.all
def test_item_attributes(test_item):
    assert test_item.name == "Test Item"
    assert test_item.price == 10.0
    assert test_item.quantity == 2


