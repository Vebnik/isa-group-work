from src.connector import Connector


df = Connector('./data/df.json')


def test_connector_insert():
  data_for_file = {'id': 1, 'title': 'tet'}

  df.insert(data_for_file)
  data_from_file = df.select({'id': 1})

  assert data_from_file == [data_for_file]
  

def test_connector_delete():
  df.delete({'id': 1})

  data_from_file = df.select({'id': 1})

  assert data_from_file == []
