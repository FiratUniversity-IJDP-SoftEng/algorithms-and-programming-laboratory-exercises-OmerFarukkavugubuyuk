# Your Student ID:230543015
# Your Name and Surname: Ömer Faruk Kavuğubüyük

from datetime import datetime

now = datetime.now()

current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime("%H:%M:%S")

print("Current date:", current_date)
print("Current time:", current_time)
print("Current date and time:", current_date , current_time)
