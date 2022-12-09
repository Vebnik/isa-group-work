import logging
import json


class GetData:
  path_to_data: str

  def __init__(self, path_to_data: str):
    self.path_to_data = path_to_data


  def get_data(self) -> list[dict]:
    try:
      with open(self.path_to_data, 'r', encoding='utf-8') as file:
        return json.loads(file.read())
    except Exception as ex:
      logging.critical(ex)