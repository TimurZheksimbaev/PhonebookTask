from typing import Dict
from src.PersonInfo import PersonInfo
from src.JsonManager import JsonManager

class Phonebook:
    """
    Класс телефонный справочник
    Обязанности:
        - записать человека в справочник
        - вывести на экран все номера
        - редактировать запись
        - удалить запись
        - найти запись
    Attributes:
    ----------
        json_manager : JsonManager()
    Methods:
    --------
        write()
            записывает данные о человеке
        print_person()
            выводит информацию об одном человеке на экран
        display()
            выводит на экран данные о всех людях в справочнике
        edit()
            редактирует запись
        delete()
            удаляет запись
        search()
            ищет оодну или более записей
    """
    def __init__(self, file_path: str):
        self.json_manager = JsonManager(file_path)

    def write(self, new_person: PersonInfo):
        """
        Записывает человека
        :param new_person: PersonInfo()
        :return: None
        """
        self.json_manager.write(new_person.to_json())

    def print_person(self, person_info: Dict[str, str]):
        """
        Выводит на экран информацию об одно человеке
        :param person_info: Dict[str, str]
        :return: None
        """
        person = PersonInfo(**person_info)
        print(f"""{person.surname} {person.name} {person.fathername}, {person.organization}\nРабочий телефон: {person.work_phone_number} \nЛичный номер: {person.personal_phone_number} 
        """)

    def display(self):
        """
        Выводит на экран все записи
        :return: None
        """
        data = self.json_manager.read()
        for person in data:
            self.print_person(person)

    def edit(self, query: Dict[str, str], change: Dict[str, str]):
        """
        Редактирует запись
        :param query: Dict[str, str]
        :param change: Dict[str, str]
        :return: None
        """
        self.json_manager.edit(query, change)

    def delete(self, query: Dict[str, str]):
        """
        Удаляет запись
        :param query: Dict[str, str]
        :return: None
        """
        self.json_manager.delete(query)

    def search(self, query: Dict[str, str]):
        """
        Ищет запись в справочнике
        :param query: Dict[str, str]
        :return: None
        """
        data = self.json_manager.search(**query)
        if not data:
            print("Не нашлось таких людей")
            exit()
        print("*********************")
        print("Похожие люди")
        for person in data:
            self.print_person(person)
        print("**********************")
