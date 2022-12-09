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
    products: list

    def __init__(self):
        pass

    def __bool__(self):
        """
        Проверяет есть ли товар в категории
        """
        pass

    def __len__(self):
        """
        Возвращает количество наименований товаров, у которых есть наличие на складе
        """
        pass