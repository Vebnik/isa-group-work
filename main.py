import logging

from src.catalog import Product, Category, Shop
from src.connector import Connector
from src.get_data import GetData


def main():
  logging.basicConfig(level=logging.INFO)

  # connector
  df_products = Connector('./data/products.json')
  data_products = df_products.get_data()

  df_categories = Connector('./data/categories.json')
  data_categories = df_categories.get_data()

  # product
  list_product = [Product(item) for item in data_products]

  # category
  for item in data_categories:
    item['products'] = list_product

  list_category = [Category(item) for item in data_categories]

  # shop
  args = {
    'products': list_product,
    'categories': list_category
  }

  shop = Shop(args)

  shop.get_product()
  shop.get_categories()
  shop.get_products()


if __name__ == '__main__':
  main()

