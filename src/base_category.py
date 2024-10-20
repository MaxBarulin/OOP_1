from abc import ABC, abstractmethod


class BaseCategory(ABC):
    """ Абстрактный метод, для классов Категория """

    @abstractmethod
    def __str__(self):
        pass