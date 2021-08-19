# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

def find_big(iterable: list):

    tmp = iterable[0]

    for i in iterable:
        if not isinstance(i, int):
            raise TypeError(f"Function not support type '{i.__class.__name__}'")

        if i > tmp:
            yield i

        tmp = i


if __name__ == '__main__':
    source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

    generator = find_big(source_list)
    print(list(generator))
