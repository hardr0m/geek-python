seconds = int(input("Введи время в секундах, от 0 до 86400: "))
hh = seconds // 3600
mm = (seconds % 3600) // 60
ss = (seconds % 3600) % 60

print("Текущее время:", hh, ":", mm, ":", ss) # не требуется по заданию

print("Текущее время: {}:{}:{}".format(hh, mm, ss))