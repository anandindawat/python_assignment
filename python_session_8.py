apps = ["Zomato", "Swiggy", "Uber Eats", "Blinkit", "Zepto"]

for app in apps:
    print(app)

steps = [6500, 8200, 9800, 10500, 12000, 9500, 11000]

i = 0

while i < len(steps):
    if steps[i] > 10000:
        print("First day crossed 10,000 steps:", i + 1)
        print("Steps:", steps[i])
        break
    i += 1

teams = ["MI", "CSK", "Royal Challengers Bangalore", "KKR", "Sunrisers Hyderabad"]

for team in teams:
    if len(team) <= 6:
        continue
    print(team)
durations = [210, 180, 245, 200]

for position, duration in enumerate(durations, start=1):
    print(f"Song {position}: {duration} seconds")

prices = [499, 799, 0, 899, 350, 600]

total = 0

for price in prices:
    if price == 0:
        continue

    total += price

    if total > 2000:
        print("Total crossed ₹2000")
        break

print("Final Total =", total)        
