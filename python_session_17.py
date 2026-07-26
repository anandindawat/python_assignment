import math

result = math.sqrt(225)
print("Square root of 225 =", result)



import os

folder_name = "MyDownloads"

os.makedirs(folder_name, exist_ok=True)

print("Absolute Path:")
print(os.path.abspath(folder_name))




from datetime import datetime

current = datetime.now()

formatted = current.strftime("%d-%m-%Y %H:%M:%S")

print("Current Date & Time:")
print(formatted)





