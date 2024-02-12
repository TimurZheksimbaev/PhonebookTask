from typing import Dict


class PersonInfo:
    """Класс PersonInfo предназначен для хранения данных о человеке в телефонном справочнике.
        Список данных:
            имя
            фамилия
            отчество
            название организации
            рабочий номер телефона
            личный номер телефона

    Attributes
    ----------
        name : str
            имя человека

        surname : str
            фамилия человека

        fathername : str
            отчество человека

        organization: str
            название организации

        work_phone_number : str
            рабочий номер телефона

        personal_phone_number : str
            личный номер телефона
    """

    def __init__(self,
                 name: str,
                 surname: str,
                 fathername: str,
                 organization: str,
                 work_phone_number: str,
                 personal_phone_number: str):
        self.name = name
        self.surname = surname
        self.fathername = fathername
        self.organization = organization
        self.work_phone_number = work_phone_number
        self.personal_phone_number = personal_phone_number

    def to_json(self):
        return self.__dict__

    def from_json(self, json_data: Dict[str, str]):
        return PersonInfo(**json_data)