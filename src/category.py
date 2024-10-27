from src.base_category import BaseCategory
from src.product import Product

class Category(BaseCategory):
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализация класса с атрибутами категории товара"""
        self.name = name
        self.description = description
        self.__products = products
        self.category_count += 1
        self.product_count += len(products)

    def __str__(self) -> str:
        self.sum_product = sum([product.quantity for product in self.__products])
        return f"{self.name}, количество продуктов: {self.sum_product} шт."

    def add_product(self, new_products):
        """Метод добавления нового продукта в класс category"""
        if isinstance(new_products, Product):
            self.__products.append(new_products)
            self.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        """Метод для получения информации о продуктах в классе Category"""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def list_products(self):
        return self.__products

    def middle_price(self):
        """Подсчет средней стоимости товаров в категории"""
        try:
            total_price_product = sum([product.price for product in self.__products])
            middle_price = total_price_product / sum([product.quantity for product in self.__products])
            return f"{round(middle_price, 2)} руб."
        except ZeroDivisionError:
            return 0