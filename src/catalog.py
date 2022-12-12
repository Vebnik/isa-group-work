import logging


class Product:
    id: int
    title: str
    price: float
    count: int
    category: int

    def __init__(self, args: dict):
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

    def __init__(self, args: dict):
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

