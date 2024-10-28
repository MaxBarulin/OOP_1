from src.order import Order


def test_order(product1):
    order1 = Order(product1)
    assert str(order1) == 'Название: Samsung Galaxy S23 Ultra, кол-во: 5 шт, итого: 900000 руб.'
