from typing import List, Dict
from src.PersonInfo import PersonInfo
import json

class JsonManager:
    def __init__(self, _file_path: str):
        self.file_path = _file_path

    def write_to_json(self, data: List[Dict[str, str]]):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=2)
        except FileNotFoundError as error:
            print(error)

    def write(self, person_info: Dict[str, str]) -> None:
        data = self.read()

        data.append(person_info)

        self.write_to_json(data)


    def read(self) -> List[Dict[str, str]]:
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

    def edit(self, query: Dict[str, str], change: Dict[str, str]):
        data = self.read()
        new_data = []
        matched = self.search(**query)
        if matched:
            for i in range(len(data)):
                if matched[0] == data[i]:
                    for key, value in change.items():
                        if value == "":
                            continue
                        data[i][key] = change[key]

            print("Edited successfully!")

        self.write_to_json(data)


    def delete(self, person: Dict[str, str]):
        data = self.read()
        matched_data = self.search(**person)
        if matched_data:
            data.remove(matched_data[0])
        self.write_to_json(data)


    def search(self, **query) -> List[Dict[str, str]]:
        data = self.read()
        matches = []

        for person in data:
            for key, value in query.items():
                if value == person[key] or value.lower() == person[key].lower():
                    matches.append(person)

        return matches