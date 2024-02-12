import sys
from typing import Dict, Tuple

from src.PersonInfo import PersonInfo
from src.Phonebook import Phonebook

def build_query() -> Dict[str, str]:
    commands = ["имя", "фамилия", "отчество", "организация", "рабочий номер телефона", "личный номер телефона"]
    commands_dict = ["name", "surname", "fathername", "organization", "work_phone_number", "personal_phone_number"]
    query = {}
    for i in range(6):
        query[commands_dict[i]] = input(commands[i] + "-> ")

    return query

def build_person() -> PersonInfo:
    commands = ["имя", "фамилия", "отчество", "организация", "рабочий номер телефона", "личный номер телефона"]
    person_info = []
    for i in range(6):
        person_info.append(input(commands[i] + "-> "))
    return PersonInfo(*person_info)

def build_with_replacement() -> Tuple[Dict[str, str], Dict[str, str]]:
    commands = ["имя", "фамилия", "отчество", "организация", "рабочий номер телефона", "личный номер телефона"]
    commands_dict = ["name", "surname", "fathername", "organization", "work_phone_number", "personal_phone_number"]
    query = {}
    change = {}
    for i in range(6):
        message = input(commands[i] + "-> ").split()
        if len(message) == 2:
            query[commands_dict[i]] = message[0]
            change[commands_dict[i]] = message[1]
        else:
            query[commands_dict[i]] = ""
            change[commands_dict[i]] = ""
    return query, change

def main():
    args = sys.argv
    file_path = args[1]
    phonebook = Phonebook(file_path)
    print(" -------------------- Добро пожаловать в телефонный справочник ---------------------")
    while True:
        print("---------------------------------------------------")
        print("-- Напишите 'create' чтобы создать новый номер")
        print("-- Напишите 'display' чтобы увидеть все номера")
        print("-- Напишите 'edit' чтобы редактировать справочник")
        print("-- Напишите 'delete' чтобы удалить номер")
        print("-- Напишите 'search' чтобы найти номер")
        print("-- Напишите 'exit' чтобы закончить или нажмите Ctrl + C")
        user_message = input("Напишите -> ")

        match user_message:
            case 'create':
                person = build_person()
                phonebook.write(person)
            case 'display':
                phonebook.display()
            case 'edit':
                print("Чтобы изменить параметры человека пишите изменения через пробел. Например: John Mark. Это значит заменить John на Mark")
                query, change = build_with_replacement()
                phonebook.edit(query, change)
            case 'delete':
                print("Напишите параметры человека -> ")
                query = build_query()
                phonebook.delete(query)
            case 'search':
                print("Напишите параметры поиска -> ")
                query = build_query()
                phonebook.search(query)
            case 'exit':
                exit(0)





if __name__ == "__main__":
    main()