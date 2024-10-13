import json
import os

from src.category import Category
from src.product import Product


def read_json_file(path_file: str) -> list[dict]:
    """Функция читает файл json"""
    json_file = os.path.abspath(path_file)
    with open(json_file, "r", encoding="utf-8") as f:
        file = json.load(f)
    return file


def create_object_from_json(file: list[dict]) -> list:
    """Функция возвращает list с обьектами product класса Category"""
    category = []
    for obj in file:
        products = []
        for product in obj["products"]:
            if isinstance(product, dict):
                products.append(Product(**product))
            else:
                products.append(product)
        obj["products"] = products
        category.append(Category(**obj))
    return category


if __name__ == "__main__":
    files = read_json_file("../data/products.json")
    print(create_object_from_json(files))
    print(create_object_from_json(files)[0].name)
    print(create_object_from_json(files)[1].name)
    print(create_object_from_json(files)[0].products)
    print(create_object_from_json(files)[1].products[0].name)
