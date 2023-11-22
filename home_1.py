import re

def decorator(func):
    def inner(*args, **kwargs):
        new_args = []
        for arg in args:
            new_arg = None
            if type(arg) == str:
                new_arg = arg
            new_args.append(new_arg)
        res = func(*new_args, **kwargs)
        return res
    return inner


@decorator
def register_stud(name,surname):
    print('Загружаем информацию')

    print(f'Имя {name}, Фамилия {surname} введены Вами. При выявлении None - исправте данные')

register_stud(10, 'Иванов')
register_stud('Изя', 'Петров')
register_stud('Коля', 20)


