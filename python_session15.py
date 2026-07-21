def get_song_duration_per_minute(total_duration, number_of_songs):
    try:
        average = total_duration / number_of_songs
        print("Average song duration:", average, "minutes")
    except ZeroDivisionError:
        print("Error: Number of songs cannot be zero.")
    finally:
        print("Calculation completed.")

# Example
get_song_duration_per_minute(120, 10)
get_song_duration_per_minute(120, 0)


try:
    total_amount = float(input("Enter total cart amount: "))
    item_count = int(input("Enter number of items: "))

    price_per_item = total_amount / item_count
    print("Price per item:", price_per_item)

except ZeroDivisionError:
    print("Error: Item count cannot be zero.")






class NoOffersApplied(Exception):
    pass

try:
    total_spend = float(input("Enter total spend: "))
    offers = int(input("Enter number of offers applied: "))

    if offers == 0:
        raise NoOffersApplied("No offers applied. Cashback cannot be calculated.")

    cashback = total_spend / offers
    print("Average cashback per offer:", cashback)

except NoOffersApplied as e:
    print("Custom Error:", e)    




def calculate_average_rating(total_rating, num_reviews):
    try:
        average = total_rating / num_reviews
        print("Average Rating:", average)
    except ZeroDivisionError:
        print("Error: Number of reviews cannot be zero.")
    finally:
        print("Thank you for using the calculator.")

calculate_average_rating(500, 0)
calculate_average_rating(500, 25)



def safe_divide_for_zomato(bill_amount, people):
    try:
        result = bill_amount / people
    except ZeroDivisionError:
        print("Error: Number of people cannot be zero.")
    else:
        print("Each person should pay:", result)
    finally:
        print("Split calculation done.")

# Example
safe_divide_for_zomato(2000, 4)
safe_divide_for_zomato(2000, 0)