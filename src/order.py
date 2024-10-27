from src.base_category import BaseCategory
from src.category import Category
from src.product import Product


class Order(BaseCategory):

    def __init__(self, product: Product):
        if product.quantity <= 0:
            raise ...
        self.product = product

    def __str__(self) -> str:
        list_price_quantity = str(self.__dict__.values()).split(",")

        total_price = list_price_quantity[-2].strip(" ")
        total_quantity = list_price_quantity[-1].strip(" )]")
        total_sum = int(total_quantity) * int(total_price.split(".")[0])

        total_name = list_price_quantity[0].split("(")[2]

        return f"Название: {total_name}, кол-во: {total_quantity} шт, итого: {total_sum} руб."


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1],
    )

    order1 = Order(product1)
    print(order1)