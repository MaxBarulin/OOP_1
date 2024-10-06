def test_init_category(category1, product1, product2):
    assert category1.name == "Смартфоны"
    assert category1.description == ("Смартфоны, как средство не только коммуникации, "
                                     "но и получения дополнительных функций для удобства жизни")
    assert len(category1.list_products) == 2
    assert category1.category_count == 1
    assert category1.product_count == 2


def test_category_product_property(category1):
    assert category1.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                  'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n')


def test_test_category_product_setter(category1, product1):
    assert len(category1.list_products) == 2
    category1.add_product(product1)
    assert len(category1.list_products) == 3


def test_category_str(category1):
    assert str(category1) == 'Смартфоны, количество продуктов: 13 шт.'
