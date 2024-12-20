import pytest

from src.product import Product
from src.exception_quantity import ExceptionQuantity
from unittest.mock import patch


def test_init_product(product1, product2):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 210000.0
    assert product2.quantity == 8


def test_create_product(new_test_product):
    test_product = Product.new_product(new_test_product)

    assert test_product.name == "Samsung Galaxy S23 Ultra"
    assert test_product.description == "256GB, Серый цвет, 200MP камера"
    assert test_product.price == 180000.0
    assert test_product.quantity == 5


def test_product_setter(capsys, product_test_setter):
    with patch('src.product.input', return_value='y'):
        product_test_setter.price = 500
        message = capsys.readouterr()
        assert message.out.split("\n")[1] == "Вы точно хотите понизить цену с 180000.0 до 500? y/n"


def test_product_setter_negative(capsys, product_test_setter):
    with patch('src.product.input', return_value='y'):
        product_test_setter.price = -1
        message = capsys.readouterr()
        assert message.out.split("\n")[1] == "Цена не должна быть нулевая или отрицательная"


def test_product_setter_null(capsys, product_test_setter):
    with patch('src.product.input', return_value='y'):
        product_test_setter.price = 0
        message = capsys.readouterr()
        assert message.out.split("\n")[1] == "Вы точно хотите понизить цену с 180000.0 до 0? y/n"


def test_product_str(product1, product2):
    assert str(product1) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'
    assert str(product2) == 'Iphone 15, 210000.0 руб. Остаток: 8 шт.'


def test_product_add(product1, product2):
    assert product1 + product2 == 2580000.0


def test_product_invalid_quantity():
    with pytest.raises(ExceptionQuantity, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)
