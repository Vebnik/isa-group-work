import logging

from src.catalog import Product, Category
from src.connector import Connector
from src.get_data import GetData


def main():
  logging.basicConfig(level=logging.INFO)

  # connector
  df = Connector('./data/df.json')
  data_select = df.select({'id': 1})

  # get data
  data = GetData('./data/products.json')
  data = data.get_data()

  # product
  list_product = [Product(item) for item in data]

  # category
  cat_data = {
    'id': 1,
    'title': 'Some Title',
    'description': 'Some description',
    'products': list_product,
  }

  category = Category(cat_data)
  
  print(category.products_list)

if __name__ == '__main__':
  main()

