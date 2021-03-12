from typing import List


class Person:
    person_id = 0
    name: str
    surname: str

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.person_id = self.person_id
        Person.person_id += 1

    def __add__(self, other):
        return Person(self.name, other.surname)

    # def __repr__(self):
    #     return f"{self.__class__.__name__} {self.person_id}: {self.name} {self.surname}"

    def __repr__(self):
        return f'{self.name} {self.surname}'

class Group:
    name: str
    people: List[Person]

    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __add__(self, other):
        return Group(f'TODO', people=self.people+other.people)

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        return f'Group {self.name} with members {", ".join(map(str, self.people))}'

    def __getitem__(self, item):
        return f"Person {item}: {self.people[item]}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(len(second_group))
print(len(third_group))
print(second_group)
print(third_group[0])
print(p0)

for person in third_group:
    print(person)
