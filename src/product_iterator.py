class ProductIter:
    """Класс для итерации products класса Category"""
    def __init__(self, category_obj: object):
        self.category = category_obj

    def __iter__(self) -> object:
        self.index = 0
        return self

    def __next__(self) -> object:
        if self.index < len(self.category.list_products):
            product = self.category.list_products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration