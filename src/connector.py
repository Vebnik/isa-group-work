import logging
import os
import json


class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None

    def __init__(self, df):
        self.__data_file = df
        self.__connect()


    def __connect(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        """
        try:
            if not os.path.exists(self.__data_file):
                with open(self.__data_file, 'w') as file:
                    file.write(json.dumps([]))
        except Exception as ex:
            logging.critical(ex)

    def get_data(self) -> list[dict]:
        try:
            with open(self.__data_file, 'r', encoding='utf-8') as f:
                return json.loads(f.read())
        except Exception as ex:
            logging.critical(ex)

    def insert(self, data_insert):
        try:
            with open(self.__data_file, 'r') as f:
                data = json.loads(f.read())
            
            with open(self.__data_file, 'w') as f:
                data.append(data_insert)
                f.write(json.dumps(data))

        except Exception as ex:
            logging.critical(ex)

    def select(self, query):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        try:
            with open(self.__data_file, 'r', encoding='utf-8') as file:
                data = json.loads(file.read())
                result = None

                for key in query.keys():
                    result = [*filter(lambda el: el[key] == query[key], result if result else data)]
                
                return result
            
        except Exception as ex:
            logging.critical(f'{ex}')

    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select
        """
        try:
            with open(self.__data_file, 'r') as f:
                data = json.loads(f.read())
            
            with open(self.__data_file, 'w') as f:
                result = None

                for key in query.keys():
                    result = [*filter(lambda el: el[key] != query[key], result if result else data)]

                f.write(json.dumps(result))

        except Exception as ex:
            logging.critical(ex)
