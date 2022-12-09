import logging

from src.catalog import Product, Category
from src.connector import Connector


def main():
  logging.basicConfig(level=logging.INFO)  

  # connector
  df = Connector('./data/df.json')
  data_for_file = {'id': 1, 'title': 'tet'}

  df.insert(data_for_file)
  data_from_file = df.select({'id': 1})

  logging.info('Try to  assert data_from_file == [data_for_file]')
  assert data_from_file == [data_for_file]
  
  df.delete({'id': 1})
  data_from_file = df.select({'id': 1})

  logging.info('Try to  assert data_from_file == []')
  assert data_from_file == []


if __name__ == '__main__':
  main()

  