songs = ["Shape Of You", "Blinding Lights", "Levitating", "Senorita"]

lowercase_songs = list(map(lambda song: song.lower(), songs))

print(lowercase_songs)


ratings = [4.2, 3.8, 4.5, 2.9, 3.5]

high_ratings = list(filter(lambda x: x > 4.0, ratings))

print(high_ratings)


from functools import reduce

prices = [499, 1299, 299, 799]

total = reduce(lambda x, y: x + y, prices)

print("Total Price =", total)


def format_followers(num):
    if num >= 1000000:
        return f"{num/1000000:.1f}M"
    elif num >= 1000:
        return f"{num/1000:.1f}K"
    else:
        return str(num)

followers = [950, 1500, 25000, 1200000]

formatted = list(map(format_followers, followers))

print(formatted)

scores = [101, 98, 120, 77, 88]

even_scores = list(filter(lambda x: x % 2 == 0, scores))

print(even_scores)