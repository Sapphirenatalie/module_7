import os
import time

directory = r"C:\Users\saffi\PycharmProjects\Lessons\Homeworks\07_module_hw"
directory_normalized = os.path.abspath(directory)

print(f'Исправленная директория:\n{directory_normalized}')
count = 0

for root, dirs, files in os.walk(directory_normalized):
    for file in files:
        count += 1
        print(f'{'<>' * 35}')
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%B.%Y %H:%M", time.localtime(filetime))
        create_time = os.path.getctime(filepath)
        formatted_create_time = time.strftime("%d.%B.%Y %H:%M", time.localtime(create_time))
        file_size = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл № {count}: {file} \nПуть:\n{filepath}\n'
              f'Размер: {file_size} байт\nВремя создания: {formatted_create_time}\n'
              f'Время изменения: {formatted_time}\nРодительская директория:\n{parent_dir}')
    print(f'{'<>' * 35}')
    print(f'\nВсего обнаружено файлов: {count}')


# Файлы в операционной системе
# Цель задания:
# Освоить работу с файловой системой в Python, используя модуль os.
# Научиться применять методы os.walk, os.path.join, os.path.getmtime,
# os.path.dirname, os.path.getsize и использование модуля time для корректного отображения времени.

# Задание:
# Создайте новый проект или продолжите работу в текущем проекте.
# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# Примените os.path.join для формирования полного пути к файлам.
# Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# Используйте os.path.getsize для получения размера файла.
# Используйте os.path.dirname для получения родительской директории файла.

# Комментарии к заданию:
# Ключевая идея – использование вложенного for
# for root, dirs, files in os.walk(directory):
#   for file in files:
#     filepath = ?
#     filetime = ?
#     formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#     filesize = ?
#     parent_dir = ?
#     print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,
#     Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

# Так как в разных операционных системах разная схема расположения папок,
# тестировать проще всего в папке проекта (directory = “.”)

# Пример возможного вывода:
# Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт,
# Время изменения: 11.11.1111 11:11, Родительская директория.
