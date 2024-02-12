from typing import List, Dict
from src.PersonInfo import PersonInfo
import json

class JsonManager:
    """Класс используемый для работы с json форматом
        - записать в файл
        - считать из файла
        - поиск в файле
        - редактирование файла
        - удаление элементов

    Attrtibutes
    -----------
        file_path : str

    Methods
    -------
        write_to_json()
            записывает данные в json файл
        write()
            записывает данные о человеке
        read()
            сичтывает из файла
        search()
            ищет в файле
        delete()
            удаляет элемент в файле
        edit()
            редактирует файл

    """
    def __init__(self, _file_path: str):
        self.file_path = _file_path

    def write_to_json(self, data: List[Dict[str, str]]):
        """
        Записывате массив данных в файл
        :param data: List[Dict[str, str]]
        :return None
        """
        try:
            with open(self.file_path, 'w') as file:
                # запись в файл
                json.dump(data, file, indent=2)
        except FileNotFoundError as error:
            print(error)

    def write(self, person_info: Dict[str, str]):
        """
        Записывает данные о человеке
        :param person_info: Dict[str, str]
        :return None
        """
        data = self.read() # сначачла прочитать

        data.append(person_info) # добавить новый объект

        self.write_to_json(data) # записать в файл


    def read(self) -> List[Dict[str, str]]:
        """
        Считывает данные из файла
        :return: List[Dict[str, str]]
        """

        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file) # прочитать файл
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

    def edit(self, query: Dict[str, str], change: Dict[str, str]):
        """
        Редактриует файл
        :param query: Dict[str, str]
        :param change: Dict[str, str]
        :return: None
        """
        data = self.read() # сначала прочитать
        matched = self.search(**query) # найти похожие объекты
        if matched:
            for i in range(len(data)):
                if matched[0] == data[i]:
                    for key, value in change.items():
                        # если изменений нет, то переходим на следующую итерацию цикла
                        if value == "":
                            continue
                        data[i][key] = change[key]

            print("Edited successfully!")

        self.write_to_json(data) # записываем в файл


    def delete(self, person: Dict[str, str]):
        """
        Удаляет элемент из файла
        :param person: Dict[str, str]
        :return: None
        """
        data = self.read()
        matched_data = self.search(**person)
        if matched_data:
            data.remove(matched_data[0]) # удаляем
        self.write_to_json(data)


    def search(self, **query) -> List[Dict[str, str]]:
        """
        Ищет элемент в файле
        :param query: **kwargs
        :return: List[Dict[str, str]]
        """
        data = self.read()
        matches = []

        # Сложность поиска O(n*k), где n - количество записей, k - количество элементов в json объекте
        for person in data:
            for key, value in query.items():
                if value == person[key] or value.lower() == person[key].lower():
                    matches.append(person)

        return matches

    def search_exact(self, data: Dict[str, str]) -> bool:
        """
        Ищет человека подходящего по всем характеристикам
        :param data: Dict[str, str]
        :return: bool
        """
        people = self.read()
        for person in people:
            for key, value in data.items():
                if value != person[key]:
                    return False

        return True



