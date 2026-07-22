class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def get_discount_price(self):
       return self.price - (self.price * 10 / 100)
class Electronic(Product):
    def get_discount_price(self):
       return self.price - (self.price * 10 / 100)



def show_final_price(item):
    print("Product Name :", item.name)
    print("Discounted Price :",item.get_discount_price())
    print()



p1 = Product("Notebook", 100)
e1 = Electronic("Laptop", 50000)

show_final_price(p1)
show_final_price(e1)



class Ticket:
    def __init__(self, movie_name, price):
        self.movie_name = movie_name
        self.price = price

    def get_final_price(self):
        return self.price


class PremiumTicket(Ticket):
    def get_final_price(self):
        return super().get_final_price() + 50



t1 = Ticket("Avengers", 200)
t2 = PremiumTicket("Avengers", 200)

print("Movie :", t1.movie_name)
print("Normal Ticket Price :", t1.get_final_price())

print()

print("Movie :", t2.movie_name)
print("Premium Ticket Price :", t2.get_final_price())        