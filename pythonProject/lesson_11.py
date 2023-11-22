# This Python file uses the following encoding: utf-8
import os, sys

menu = {
    1: 'Использовать калькулятор',
    2: 'показать все опперации',
    10: 'Выход'
}
operations_log = []
FIlE_NAME = 'operations_archive.txt'
def calculate():
    number1 = int(input('Введите первое значение: '))
    znak = input('Введите знак: ')
    number2 = int(input('Введите второе значение: '))
    res = 'Что то пошло не по плану'
    if znak == '+':
        res = f'{number1} {znak} {number2} = {number1 + number2}'
    elif znak == '-':
        res = f'{number1} {znak} {number2} = {number1 - number2}'
    elif znak == '*':
        res = f'{number1} {znak} {number2} = {number1 * number2}'
    elif znak == '/':
        res = f'{number1} {znak} {number2} = {number1 / number2}'
    print(res)
    operations_log.append(res)


def show_operations():
    print('=' * 20)
    for counter, operations in enumerate(operations_log):
        print(f"{counter}, {operations}" .replace('\n', ''))
    print('=' * 20)
def run():
    with open(FIlE_NAME, 'r') as file:
        operations_log.extend(file.readlines())
    while True:
        print('Меню: ', menu )
        choose_menu_item = int(input('Выберите пункт из меню'))
        if choose_menu_item == 1:
            calculate()
        elif choose_menu_item == 2:
            show_operations()
        elif choose_menu_item == 10:
            with open(FIlE_NAME, "w") as file:
                for operation in operations_log:
                    file.write(operation.replace('\n', '') + '\n' )

            return
        else:
            print('Такого пункта меню не существует, читай внимательнее!')


run()

