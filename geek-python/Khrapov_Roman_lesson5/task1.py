# Создать программно файл в
# текстовом формате, записать в него построчно данные, вводимые пользователем.\
# Об окончании ввода данных свидетельствует пустая строка.

filename = []

while True:
    line = input("Введите произвольную строку: ")
    if line == '':
        print(filename)
        exit()
    else:
        newline = line + '\n'
        filename.append(newline)

    with open("task1.txt", "w") as file_obj:
        file_obj.writelines(filename)