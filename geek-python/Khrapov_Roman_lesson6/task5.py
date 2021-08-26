# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


def display_count():
    print('Всего сотрудников: %d' % Employee.emp_count)


class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_employee(self):
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))

emp1 = Employee("Акакий", 100000)

emp2 = Employee("Фёкла", 90000)
emp3 = Employee("Пафнутий", 95000)
emp4 = Employee("Алистарх", 80000)
emp5 = Employee("Турбина№6", 1000000)
emp1.display_employee()
emp2.display_employee()
emp3.display_employee()
emp4.display_employee()
emp5.display_employee()

print("Всего сотрудников: %d" % Employee.emp_count)