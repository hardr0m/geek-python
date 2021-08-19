# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from typing import Iterable, Callable
from itertools import filterfalse


def my_filterfalse(func: Callable, iterable: Iterable) -> None:
    def default_func(x):

        return x

    func = func if func is not None else default_func

    for i in iterable:
        if not func(i):
            yield i


if __name__ == '__main__':
    input_data = input('Пожалуйста введите целые числа разделяя их пробелами: ')

    try:
        source_list = tuple(map(int, input_data.split()))
    except ValueError:
        print('Неверно введенные данные')
        exit(1)

    # source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

    print('itertools', list(filterfalse(lambda x: source_list.count(x) > 1, source_list)))
    print('custom drophile', list(my_filterfalse(lambda x: source_list.count(x) > 1, source_list)))