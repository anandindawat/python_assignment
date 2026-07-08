insta_followers = {
    "Cristino Ronaldo": "120M",
    "Lionel Messi": "90M",
    "Selena Gomez": "45M",
    "Kylie Jenner": "43M",
    "Virat Kohli": "32M"
}
print(insta_followers)

insta_followers["Narendra Modi"] = "90M"
print(insta_followers)

insta_followers["Virat Kohli"] = "33M"
print(insta_followers)

del insta_followers["Cristino Ronaldo"]

print(insta_followers)



Food_price = {
    "Pizza":250,
    "Burger":200,
    "Pasta":300,
    "Salad":150,
    "Fries":100
}
print(Food_price)

for x,y in Food_price.items():
    if y > 200:
        print(x,y)


flipkart_users ={"jaydeep","anand","anas","mihir","dhruv"}       
myntra_users = {"dhruv","mihir","anand","aastha","vidhi"}
print(flipkart_users.intersection(myntra_users))

def get_unique_artists(spotify_playlist1,spotify_playlist2):  
    return spotify_playlist1.union(spotify_playlist2)
spotify_playlist1 ={"sidhu moosewala","arijit","armaan","ap dhillon","shreya ghosal"}  
spotify_playlist2 = {"arijit","armaan","sonu nigam","lisa","shreya ghosal"}
unique_artists = get_unique_artists(spotify_playlist1,spotify_playlist2)

print("unique_artists:",unique_artists)
    
