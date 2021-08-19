# import sys
import sys
from sys import argv

file_name, work_time, hours_pay, prem = sys.argv

print(f"Заработная плата {int(work_time) * int(hours_pay) + int(prem)} рублей")

