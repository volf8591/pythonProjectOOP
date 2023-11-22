from abc import ABC, abstractmethod
import os
import pandas
import datetime
import json
from entities import Student
class StudentsRepo(ABC):
    @abstractmethod
    def load_students(self):
        pass

    # @abstractmethod
    # def show_menu(self):
    #     pass
    #
    # @absdeftractmethod
    # def show_student_info(self):
    #     pass
    #
    # @abstractmethod
    # def save_data(self):
    #     pass

class StudentsRepoXlsx(StudentsRepo):
    STUDENTS_FILE_NAME = 'marks.xlsx'
    CONFIG_FILE_NAME = 'initial_config.json'

    def updata_wit_initial_students(self, students):
        new_students = {}
        with open(self.STUDENTS_FILE_NAME, 'r+', encoding='utf-8') as fp:
            data = json.load(fp)
            initial_students = data['users']

        for login, data in initial_students.items():
            if login in students:
                marks = students[login]
                student = Student(
                    name=login,
                    password=data['password'],
                    role=data['role'],

                    marks=marks
                )
            else:
                student = Student(
                    name=login,
                    password=data['password'],
                    role=data['role'],
                )
            new_students[login] = student
        return new_students
    def load_students(self):
        students = {}
        if os.path.exists(self.STUDENTS_FILE_NAME):
            xlsx_data = pandas.ExcelFile(self.STUDENTS_FILE_NAME)
            for sheet in xlsx_data.sheet_names:
                df1 = pandas.read_excel(xlsx_data, sheet)
                marks = df1.values.tolist()
                students[sheet] = list(
                    map(
                        lambda el:
                        (
                            datetime.datetime(
                                year=int(el[0][:4]),
                                month=int(el[0][5:7]),
                                day=int(el[0][8:10]),
                                hour=int(el[0][11:13]),
                                minute=int(el[0][14:16]),
                                second=0
                            ),
                            el[1]),
                        marks
                    )
                )
        return self.updata_wit_initial_students(students)
