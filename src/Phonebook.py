from typing import Dict
import json
from src.PersonInfo import PersonInfo
from src.JsonManager import JsonManager

class Phonebook:
    def __init__(self, file_path: str):
        self.json_manager = JsonManager(file_path)

    def write(self, new_person: PersonInfo):
        self.json_manager.write(new_person.to_json())

    def print_person(self, person_info: Dict[str, str]):
        person = PersonInfo(**person_info)
        print(f"""{person.surname} {person.name} {person.fathername}, {person.organization}\nРабочий телефон: {person.work_phone_number} \nЛичный номер: {person.personal_phone_number} 
        """)

    def display(self):
        data = self.json_manager.read()
        for person in data:
            self.print_person(person)

    def edit(self, query: Dict[str, str], change: Dict[str, str]):
        self.json_manager.edit(query, change)

    def delete(self, query: Dict[str, str]):
        self.json_manager.delete(query)

    def search(self, query: Dict[str, str]):
        data = self.json_manager.search(**query)
        if not data:
            print("Не нашлось таких людей")
            exit()
        print("*********************")
        print("Похожие люди")
        for person in data:
            self.print_person(person)
        print("**********************")
