with open("playlist.txt", "w") as file:
    file.write("Kesariya\n")
    file.write("Apna Bana Le\n")
    file.write("Tum Hi Ho\n")
    file.write("Heeriye\n")
    file.write("Satranga\n")

print("playlist.txt created successfully!")



with open("playlist.txt", "r") as file:
    for song in file:
        print(song.strip().upper())





import csv

with open("ipl.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print("Winner:", row["winner"])







from pathlib import Path
import json

file_path = Path("my_fav_apps.json")

if not file_path.exists():
    apps = [
        {"name": "Instagram", "category": "Social Media"},
        {"name": "Paytm", "category": "Finance"},
        {"name": "Zomato", "category": "Food Delivery"}
    ]

    with open(file_path, "w") as file:
        json.dump(apps, file, indent=4)

    print("JSON file created.")
else:
    print("File already exists.")