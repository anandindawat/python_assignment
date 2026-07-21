class playlist:
    def __init__(self):
        self.__song = []
    def add_song(self,song):
        self.__song.append(song)
    def show_playlist(self):
        print("plylist:",self.__song)
        
p = playlist()
p.add_song("Keshariya")
p.add_song("Not Guilty") 
p.add_song("Dil De Baithi")       
p.show_playlist()



# Build a Product class for a Flipkart-style app with a private attribute _price. Implement get_price() and set_price() methods to access and update the price. Demonstrate setting and getting the price for a product object.
class Product:
    def __init__(self,price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self,price):
        self.__price = price

product = Product(300)
print("Current price:",product.get_price())
product.set_price(400)
print("Updated price:",product.get_price())


class Movie:
    def __init__(self):
        self.__rating = 0

    def set_rating(self,rating):
        if 0 <= rating <= 10:
            self.__rating = rating
        else:
            print("invalid value is given")

    def get_rating(self):
        return self.__rating         

movie = Movie()
movie.set_rating(6.5)
print("Movie rating:",movie.get_rating())
movie.set_rating(5.6)
print("Movie rating:",movie.get_rating())


from abc import ABC,abstractmethod

class paymentmethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class Paytm(paymentmethod):
    def pay(self,amount):
        print(f"paid {amount} using paytm")

class Phonepe(paymentmethod):
    def pay(self,amount):
        print(f"paid {amount} using phonepe")    
paytm = Paytm()
phonepe = Phonepe()
paytm.pay(100)
phonepe.pay(200)                