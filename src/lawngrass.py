from src.product import Product


class LawnGrass(Product):
    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            country: str,
            germination_period: str,
            color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other) -> object:
        """Метод для подсчета общей суммы всех продуктов в данном классе"""
        if type(other) is LawnGrass:
            self.total = self.price * self.quantity
            self.total += other.price * other.quantity
            return self.total
        raise TypeError
