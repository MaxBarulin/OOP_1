from src.product import Product


class Smartphone(Product):
    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: float,
            model: str,
            memory: int,
            color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other) -> object:
        """Метод для подсчета общей суммы всех продуктов в данном классе"""
        if type(other) is Smartphone:
            self.total = self.price * self.quantity
            self.total += other.price * other.quantity
            return self.total
        raise TypeError
