import os.path
import os

def create_file(file_name):
    with open(file_name, "w") as file:
        for i in range(1, 100):
            file.write(f"Строка номер: {i}\n")

def creat_folder(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def muve_file(old_path, new_path):
    os.rename(old_path, new_path)



create_file('test_text.txt')
creat_folder(r'test_folder')
muve_file('test_text.txt', 'test_folder/test_text.txt')