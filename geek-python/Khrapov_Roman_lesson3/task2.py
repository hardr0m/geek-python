# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_list(**user_list):

    print(f'Имя: {user_list.get("first_name")}, фамилия: {user_list.get("last_name")},'
          f' год рождения: {user_list.get("byear")}, город проживания: {user_list.get("city")},'
          f' email: {user_list.get("email")}, телефон: {user_list.get("phone")}')


if __name__ == '__main__':
    user = dict(first_name='Ivan', last_name='Ivanov', byear='1980', city='Bobruysk', email='1@mail.ru',
                phone='893456789')

    user_list(**user)
