# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(arg_1, arg_2):
    try:
        quotient = arg_1 / arg_2
        return quotient
    except ZeroDivisionError:
        return "Cannot be divided by zero"
    except ValueError:
        return "ValueError"


print(my_func(int(input("divider = ")), int(input("dividend = "))))
