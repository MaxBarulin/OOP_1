from src.base_product import BaseProduct
from src.exception_quantity import ExceptionQuantity
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для создания класса продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация класса с атрибутами продукта"""
        self.name = name
        self.description = description
        self.__price = price
        if quantity <= 0:
            raise ExceptionQuantity("Товар с нулевым количеством не может быть добавлен")
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> object:
        """Метод для подсчета общей суммы всех продуктов в данном классе"""
        self.total = self.__price * self.quantity
        self.total += other.__price * other.quantity
        return self.total

    @classmethod
    def new_product(cls, params_product: dict) -> object:
        """Метод создания нового класса product"""
        return cls(
            name=params_product["name"],
            description=params_product["description"],
            price=params_product["price"],
            quantity=params_product["quantity"]
        )

    @property
    def price(self) -> object:
        return self.__price

    @price.setter
    def price(self, prices) -> None:
        """Метод контроля изменения цены"""
        if prices <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif prices < self.__price:
            print(f"Вы точно хотите понизить цену с {self.__price} до {prices}? y/n\n")
            user = input()
            if user == "y":
                if prices <= 0:
                    print("Цена не должна быть нулевая или отрицательная")
                    return
                self.__price = prices
            return
