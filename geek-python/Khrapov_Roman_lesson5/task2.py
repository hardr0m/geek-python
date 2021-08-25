# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_list = ['Акакий\n', 'Пафнутий\n', 'Алистарх\n']
with open("task2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("task2.txt") as file_obj:
    a = 0
    b = 0
    for i in file_obj:
        a += i.count("\n")
        b = len(i)-1
        print(f"{b} letters in line")
    print(f"String count is {a}")