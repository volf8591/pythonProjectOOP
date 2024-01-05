from dataclasses import dataclass
class MainSaver:
    def __init__(self, login, password):
        self.login = login
        self.password = password
    def main_save(self):
        print(f'[{self.login} - {self.password}] Основное сохранение: {self}')

class XLSXSaver:
    def __init__(self):
        pass
    def save_to_exsel(self):
        print(f'Сохранено в EXSEL: {self}')
class DbSaver:
    def __init__(self):
        pass
    def save_to_db(self):
        print(f'Сохранено в Базу данных: {self}')


class Car(MainSaver, DbSaver, XLSXSaver):
    def __init__(self, model, year):
        super().__init__('login1', 'password1')
        self.model = model
        self.year = year

    def __repr__(self):
        return f'{self.model} {self.year}'

class Student(MainSaver, DbSaver, XLSXSaver):
    def __init__(self, name, last_name):
        super().__init__('login2', 'password2')
        self.name = name
        self.last_name = last_name

    def __repr__(self):
        return f'{self.name} {self.last_name}'

car = Car('Ferari SF 900', 2018)
student = Student('Иван', 'Петров')
to_save_elems = [car, student]

for elem in to_save_elems:
    elem.main_save()
    elem.save_to_db()
    elem.save_to_exsel()


# print(Student.__mro__)
