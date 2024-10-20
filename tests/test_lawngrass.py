import pytest


def test_grass_init(test_grass1):
    assert test_grass1.name == "Газонная трава"
    assert test_grass1.description == "Элитная трава для газона"
    assert test_grass1.price == 500.0
    assert test_grass1.quantity == 20
    assert test_grass1.country == "Россия"
    assert test_grass1.germination_period == "7 дней"
    assert test_grass1.color == "Зеленый"


def test_add_grass(test_grass1, test_grass2):
    assert test_grass1 + test_grass2 == 16750.0


def test_add_grass_error(test_grass1):
    with pytest.raises(TypeError):
        result = test_grass1 + 1
