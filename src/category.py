class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализация класса с атрибутами категории товара"""
        self.name = name
        self.description = description
        self.__products = products
        self.category_count += 1
        self.product_count += len(products)

    def add_product(self, new_products):
        self.__products.append(new_products)
        Category.product_count += 1

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    @property
    def list_products(self):
        return self.__products
