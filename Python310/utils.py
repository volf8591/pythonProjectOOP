import random

class Utils:
    ADMIN_ACCESS = 'ADMIN ACCESS'
    STUDENT_ACCESS = 'STUDENT_ACCESS'
    @staticmethod
    def show_menu(student):
        try:
            chosen_item = int(input('Выберите пункт меню: '))
            if access_role == STUDENT_ACCESS and chosen_item == 1:
                start_test(login)
            elif access_role == ADMIN_ACCESS and chosen_item == 10:
                print('Программа завершила работу')
                return
            elif access_role == STUDENT_ACCESS and chosen_item == 10:
                print('Все данные успешно сохранены')
                save_data()
                return
            elif access_role == ADMIN_ACCESS and chosen_item == 1:
                show_everage_info()
            elif access_role == ADMIN_ACCESS and chosen_item == 2:
                show_student_info()

        except Exception as e:
            print('Такого пункта меню не существует')

    @staticmethod
    def try_to_show_menu(student):
        Utils.show_menu(student) if student is not None else print('Ты не смог залогинится в программе')



    @staticmethod
    def input_login_pass():
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        return login, password
    @staticmethod
    def check_is_registered(students, login, password):
        res = None
        if login.lower() in students.keys():
            student = students[login.lower()]
            valid_password = student.password
            if password == valid_password:
                res = student
        return res


    @staticmethod
    def generate_random_test():
        number1 = random.randint(1, 10)
        znak = ['-', '+', '*'][random.randint(0, 2)]
        number2 = random.randint(1, 10)
        question = f'{number1} {znak} {number2}'
        return question, eval(question)