# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
import sys

my_list = ['Акакий\n', 'Пафнутий\n', 'Алистарх\n']
with open("task2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("task2.txt") as file_obj:
    a = 0
    b = 0
    for line in file_obj:
        a += line.count("\n")
        b = len(line) - 1
        print(f"{b} Количество букв в строке")
    print(f"Количество строк {a}")
