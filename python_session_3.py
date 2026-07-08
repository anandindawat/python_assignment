name = "Anand pal singh"
age = 22
height = 5.6
spotify_account = True

print(name)
print(type(name))

print(age)
print(type(age))

print(height)
print(type(height))

print(spotify_account)
print(type(spotify_account))


def total_cart_amount(prices):
    total = 0.0
    for price in prices:
        total = total + float(price)
    return total

prices = ["199.99","49","350.75"]
print(total_cart_amount(prices))

score = input("Enter your score:")
score = int(score)
if score == 50:
    print("Half century!")
else:
    print("Keep going")


is_premium = "True"
is_premium = (is_premium == "True")
print(is_premium)
print(type(is_premium))                             


s_premium = "False"
is_premium = (is_premium == "False")
print(is_premium)
print(type(is_premium))                             