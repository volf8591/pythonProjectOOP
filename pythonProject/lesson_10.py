# Запись с удалением предыдущей информации
with open("text_info.txt", "w") as file:
    for i in range(1, 100):
        file.write(f"Строка номер: {i}\n")

# Читаем файл
with open("text_info.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.replace('\n', ''))

# Дописываем файл не удаляя содержимое
with open("text_info.txt", "a") as file:
    file.write(f"Еще одна строка в конец файла: \n")
    file.write(f"Еще одна строка в конец файла: \n")
    file.write(f"Еще одна строка в конец файла: \n")

# Дописываем файл, не удаляя содержимое
with open('new_file.txt', "x") as file:
    file.write(f"XXXXXXXXXXXXXXXXXXX\n")