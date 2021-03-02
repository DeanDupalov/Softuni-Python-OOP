from calendar import month_name
from typing import List, Optional


class DVD:
    name: str
    id: int
    creation_year: int
    creation_month: str
    age_restriction: int
    is_rented: bool

    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}. Status: {self.is_rented_sting()}"

    def is_rented_sting(self) -> str:
        if self.is_rented:
            return 'rented'
        return 'not rented'

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int) -> Optional['DVD']:
        date_info = cls.separate_date(date) # "23.12.2020"
        return cls(name, id, int(date_info[2]), month_name[int(date_info[1])], age_restriction)

    @staticmethod
    def separate_date(date: str) -> List:
        date_list = date.split('.')
        return date_list