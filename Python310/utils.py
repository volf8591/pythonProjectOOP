import random

class Utils:
    ADMIN_ACCESS = 'ADMIN ACCESS'
    STUDENT_ACCESS = 'STUDENT_ACCESS'
    INVALID_CREDENTIALS = 'INVALID_CREDENTIALS'
    @staticmethod
    def input_login_pass():
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        return login, password
    @staticmethod
    def check_is_registered(students, login, password):
        # if login.lower() in logins.keys():
        #     valid_password = logins[login.lower()][0]
        #     if password == valid_password:
        #         return logins[login.lower()][1], login
        #         else:
        #             return INVALID_CREDENTIALS, login
        #     else:
        #         return INVALID_CREDENTIALS, login
        pass


    @staticmethod
    def generate_random_test():
        number1 = random.randint(1, 10)
        znak = ['-', '+', '*'][random.randint(0, 2)]
        number2 = random.randint(1, 10)
        question = f'{number1}{znak}{number2}'
        return question, eval(question)