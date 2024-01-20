from src.phone import Phone
import pytest

@pytest.fixture
def test_item_phone():
    return Phone(name="Test Item", price=10.0, quantity=2, number_of_sim=1)

def test___repr__(test_item_phone):
    assert f'("{test_item_phone.name}", {test_item_phone.price}, {test_item_phone.quantity}, {test_item_phone.number_of_sim})'

def test___str__(test_item_phone):
    assert f'{test_item_phone.name}'
def test_number_of_sim_zero(test_item_phone):
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        test_item_phone.number_of_sim = 0

def test_number_of_sim_valid(test_item_phone):
    assert test_item_phone.number_of_sim == 1

def test_number_of_sim_negative(test_item_phone):
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        test_item_phone.number_of_sim = -1


