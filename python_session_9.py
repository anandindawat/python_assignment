def calculate_final_price(price, discount_rate):
    final_price = price - (price * discount_rate / 100)
    return final_price

price = float(input("Enter Price: "))
discount = float(input("Enter Discount Rate (%): "))

print("Final Price =", calculate_final_price(price, discount))




def get_delivery_charge(amount, city="Ahmedabad"):
    if city == "Ahmedabad":
        return 0
    else:
        return 50

amount = float(input("Enter Order Amount: "))
city = input("Enter City: ")

print("Delivery Charge =", get_delivery_charge(amount, city))




def format_price(price, currency="INR"):
    if currency == "INR":
        return f"₹{price}"
    elif currency == "USD":
        return f"${price}"
    else:
        return f"{price}"

price = float(input("Enter Price: "))
currency = input("Enter Currency (INR/USD): ")

print("Formatted Price =", format_price(price, currency))





def apply_coupon(price, coupon_code=None):
    if coupon_code == "ZOMATO10":
        return price - (price * 10 / 100)
    else:
        return price

price = float(input("Enter Price: "))
coupon = input("Enter Coupon Code: ")

print("Final Price =", apply_coupon(price, coupon))