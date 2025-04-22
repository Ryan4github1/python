import datetime
from datetime import date,time
print("current date and time: ")
print(datetime.datetime.now())
print("year:")
print(datetime.datetime.today().year)
print("months: ")
print(datetime.datetime.today().month)
print("date: ")
print(datetime.datetime.today().day)
current_time= datetime.datetime.now().strftime("%H:%M:%S")
print("current_time: ")
print(current_time)