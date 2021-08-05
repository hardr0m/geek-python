# Пользователь вводит время в секундах. Переведите
# время в часы, минуты и секунды и выведите в формате
# чч:мм:сс. Используйте форматирование строк.
enter_time_in_sec = int(input("Введите время в секундах"))
hours = enter_time_in_sec // 3600
minutes = (enter_time_in_sec - hours * 3600) // 60
seconds = enter_time_in_sec - (hours * 3600 + minutes * 60)
#print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")
print("{}:{}:{}".format(hours, minutes, seconds))

