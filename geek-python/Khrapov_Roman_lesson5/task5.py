# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
filename = "task5.txt"

num = "8 10.5 99 33 1 56 34.8 6 78 51.9 "


if __name__ == "__main__":
    summ = 0

    try:
        with open(filename, 'w+', encoding='utf-8') as a:
            a.write(num)

        with open(filename, encoding='utf-8') as a:
            data = a.read()

        for item in data.split():
            summ += float(item)
    except IOError as b:
        print(b)
    except ValueError:
        print("Неконсистентные данные")

    print(summ)
