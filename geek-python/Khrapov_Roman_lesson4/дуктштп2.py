from math import factorial


def fact(n):
    fact_list = [factorial(x) for x in range(1, n + 1)]
    yield fact_list


n = int(input("Введите число "))
for el in fact(n):
    print(el)
