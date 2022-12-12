import logging

from src.connector import Connector


class Product:
    id: int
    title: str
    price: float
    count: int
    category: int

    def __init__(self, args: dict) -> None:
        self.id = args.get('id')
        self.title = args.get('title')
        self.price = args.get('price')
        self.count = args.get('count')
        self.category = args.get('category')

    def __bool__(self):
        """
        Проверяет есть ли товар в наличии
        """
        return True if self.count > 0 else False

    def __len__(self):
        """
        Возвращает количество товара на складе
        """
        return self.count


class Category:
    id: int
    title: str
    description: str
    products_list: list[Product]

    def __init__(self, args: dict) -> None:
        self.id = args.get('id')
        self.title = args.get('ttile')
        self.description = args.get('description')
        self.products = args.get('products')

    @property
    def products(self):
        return self.products_list

    @products.setter
    def products(self, data):
        if isinstance(data[0], Product) and data:
            res = [item for item in data if item.category == self.id]
            self.products_list = res
        else:
            logging.critical('Error in setter products')
            
    def __bool__(self):
        """
        Проверяет есть ли товар в категории
        """
        return True if len(self.products) else False

    def __len__(self):
        """
        Возвращает количество наименований товаров, у которых есть наличие на складе
        """
        return len([item for item in self.products if item.count])


class Shop:
    """
    Класс для работы с магазином
    """
    products: list[Product]
    categories: list[Category]

    def __init__(self, args: dict) -> None:
        self.products = args.get('products')
        self.categories = args.get('categories')

    def __valid_category(self, cat_id: int) -> bool:
        return cat_id not in [category.id for category in self.categories]

    def __valid_product(self, prod_id: int) -> bool:
        return prod_id not in [product.id for product in self.products]

    def get_categories(self):
        """
        Показать все категории пользователю в произвольном виде, главное, чтобы пользователь
        мог видеть идентификаторы (id) каждой категории
        """
        try:
            for item in self.categories:
                print(f"id: {item.id} | description: {item.description}")

        except Exception as ex:
            logging.critical(ex)

    def get_products(self):
        """
        Запросить номер категории и вывести все товары, которые относятся к этой категории
        Обработать вариант отсутствия введенного номера
        """

        try:
            cat_id = int(input('Category id: '))

            if self.__valid_category(cat_id):
                print('Not valid category id')
                return self.get_products()

            for item in self.products:
                if item.category == cat_id:
                    print(f"title: {item.title} | count: {item.count}")

        except Exception as ex:
            logging.critical(ex)

    def get_product(self) -> None:
        """
        Запросить ввод номера товара и вывести всю информацию по нему в произвольном виде
        Обработать вариант отсутствия введенного номера
        """
        try:
            prod_id = int(input('Product id: '))

            if self.__valid_product(prod_id):
                print('Not valid product id')
                return self.get_product()

            for item in self.products:
                if item.id == prod_id:
                    print(f"id: {item.id} | title: {item.title}")

        except Exception as ex:
            logging.critical(ex)
            self.get_product()

        