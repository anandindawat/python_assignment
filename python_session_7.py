listening_time = int(input("Enter your Spotify listening time (minutes): "))

if listening_time > 120:
    print("You are a true music fan!")
else:
    print("Keep listening!")



order_amount = float(input("Enter your Zomato order amount: "))

if order_amount > 300:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")



cart_total = float(input("Enter your Flipkart cart total: "))

if cart_total > 2000:
    print("You get a 10% discount")
elif cart_total > 1000:
    print("You get a 5% discount")
else:
    print("No discount available")



points = int(input("Enter your IPL fantasy team points: "))

if points > 800:
    print("Champion")
else:
    if points >= 500:
        print("Top Performer")
    else:
        print("Keep Trying")