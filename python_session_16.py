apps = ["Zomato", "Swiggy", "Domino's", "Pizza Hut", "Uber Eats"]

it = iter(apps)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))



def playlist_generator(songs):
    for song in songs:
        yield song

songs = ["Kesariya", "Apna Bana Le", "Heeriye", "Tum Hi Ho", "Satranga"]

playlist = playlist_generator(songs)

for song in playlist:
    print(song)





cart = ["Pizza", "Burger", "Fries", "Coke"]

for index, item in enumerate(cart, start=1):
    print(index, "-", item)




teams = ["Mumbai Indians", "Chennai Super Kings", "Royal Challengers Bangalore"]
points = [18, 16, 14]

for team, point in zip(teams, points):
    print(f"Team: {team}, Points: {point}")




def order_id_generator():
    order_id = 1001
    while True:
        yield order_id
        order_id += 1

orders = order_id_generator()

print(next(orders))
print(next(orders))
print(next(orders))
print(next(orders))
print(next(orders))