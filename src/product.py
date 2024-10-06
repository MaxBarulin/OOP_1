class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация класса с атрибутами продукта"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, params_product: dict):
        return cls(
            name=params_product["name"],
            description=params_product["description"],
            price=params_product["price"],
            quantity=params_product["quantity"]
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, prices):
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
