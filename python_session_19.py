
class Song:
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

    def display(self):
        print("Song Details")
        print("Title :", self.title)
        print("Artist:", self.artist)
        print("Duration:", self.duration, "seconds")

    def play_preview(self):
        print(f"Playing 30-second preview of '{self.title}' by {self.artist}")


# Object Creation
song1 = Song("Believer", "Imagine Dragons", 204)

song1.display()
song1.play_preview()

# Duration default value example
song2 = Song("Perfect", "Ed Sheeran")
song2.display()



class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    def display(self):
        print("Restaurant:", self.restaurant_name)
        print("Items:", self.items)
        print("Total Price: ₹", self.total_price)

    def add_item(self, item_name, item_price):
        self.items.append(item_name)
        self.total_price += item_price
        print(f"{item_name} added successfully.")


# Object Creation
order = FoodOrder(
    "Zomato",
    ["Burger", "French Fries"],
    250
)

print("Original Order")
order.display()

print("\nAdding Items...")
order.add_item("Cold Drink", 50)
order.add_item("Ice Cream", 80)

print("\nUpdated Order")
order.display()