# pip install XlsxWriter

import xlsxwriter
import datetime

# date_now = datetime.datetime.now()
# print(date_now)
# print(f'Год: {date_now.year}')
# print(f'Месяц: {date_now.month}')
# print(f'Число: {date_now.day}')
# print(f'Часы: {date_now.hour}')
# print(f'Минуты: {date_now.minute}')
# print(f'Секунды: {date_now.second}')
# print(date_now - datetime.timedelta(days=3))
# print(date_now + datetime.timedelta(days=3))
date_now = datetime.datetime.now()

students = {
    'Петров': {
        'Математика': [
            (date_now - datetime.timedelta(days=5), 9),
            (date_now - datetime.timedelta(days=3), 3),
            (date_now, 8)
        ],
        'Физика':[
            (date_now - datetime.timedelta(days=10), 5),
            (date_now - datetime.timedelta(days=3), 7),
            (date_now, 8)
        ],
    },
    'Сидорова': {
        'Математика':[
            (date_now - datetime.timedelta(days=5), 6),
            (date_now - datetime.timedelta(days=3), 8),
            (date_now, 8)
        ],
        'Физика': [
            (date_now - datetime.timedelta(days=10), 3),
            (date_now - datetime.timedelta(days=3), 7),
            (date_now - datetime.timedelta(days=1), 8),
            (date_now, 10)
        ]
    }
}

# создаем файл и страничку.
workbook = xlsxwriter.Workbook('test_files.xlsx')
worksheet = workbook.add_worksheet('Петров')
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'Дата', bold)
worksheet.write('B1', 'Математика', bold)
worksheet.write('C1', 'Физика', bold)

# Запись дат
worksheet.write('A2', str(date_now - datetime.timedelta(days=10))[:10]),
worksheet.write('A3', str(date_now - datetime.timedelta(days=5))[:10]),
worksheet.write('A4', str(date_now - datetime.timedelta(days=3))[:10]),
worksheet.write('A5', str(date_now - datetime.timedelta(days=1))[:10]),
worksheet.write('A6', str(date_now)[:10]),

# Запись отметок
worksheet.write('B3', 9)
worksheet.write('B4', 3)
worksheet.write('B6', 8)

# Запись отметок
worksheet.write('C2', 5)
worksheet.write('C4', 7)
worksheet.write('C6', 8)


workbook.close()