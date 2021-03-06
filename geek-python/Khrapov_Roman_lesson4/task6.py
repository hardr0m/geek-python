# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
#     Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from typing import Iterable
from itertools import cycle


def get_repeated(iterable: Iterable, count: int):

    if not isinstance(count, int):
        raise TypeError(f"count '{count.__class__.__name__}' is illegat type")

    if count < 0:
        raise ValueError(f"count 'can't be less than 0")

    # убираем брекется и получаем стандартный режим работы sycle
    iterator = cycle([iterable])

    while count:
        yield next(iterator)
        count -= 1


if __name__ == '__main__':
    input_data = input('Пожалуйста введите целые числа разделяя их пробелами (максимум 4 числа): ')
    repeate = input('Сколько раз повторить выше введенную последовательность?: ')

    try:
        source_list = [int(i) for i in input_data.split()][:4]
        repeate = int(repeate)
    except ValueError:
        print('Неверно введенные данные')
        exit(1)

    print(list(get_repeated(source_list, repeate)))
