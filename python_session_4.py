string = "Flipkart-Sale2024"
print(string.lower())
print(string.replace("-"," "))


product_name =  "OnePlus Nord-CE 3"
print(product_name.strip().upper().replace("-",":"))


def split_product_code(split_product_code):
    return split_product_code.split("-")
print(split_product_code("ZOMATO-FOOD-2024"))


str1 = "Spotify_Premium_Offer"
print(str1[8:15])

product = 'Myntra Shirt'
price = 799.5
msg = "Deal: {} is available at ₹{:.2f}only!".format(product,price)
print(msg)
