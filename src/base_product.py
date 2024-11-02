from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс, для класса Продуктов"""

    @abstractmethod
    def __add__(self, other):
        pass
