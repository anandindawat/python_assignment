import re

text = "Call me at +91-9876543210 or +91-9123456789."

numbers = re.findall(r"\+91-\d{10}", text)

print(numbers)


import re

def check_date(text):
    pattern = r"\b\d{2}/\d{2}/\d{4}\b"
    return bool(re.search(pattern, text))

print(check_date("Today's date is 23/07/2026"))
print(check_date("No date here"))


import re

text = "Laptop Rs. 50000, Mouse Rs. 1200, Keyboard Rs. 2500"

prices = re.findall(r"Rs\.\s*(\d+)", text)

prices = [int(price) for price in prices]

print("Prices:", prices)
print("Total:", sum(prices))


import re

text = "Contact us at support@gmail.com or admin@yahoo.com"

result = re.sub(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", "[hidden email]", text)

print(result)



import re

with open("comments.txt", "r") as file:
    text = file.read()

usernames = re.findall(r"@[A-Za-z0-9_]{3,}", text)

unique_usernames = sorted(set(usernames))

print(unique_usernames)