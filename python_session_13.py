def print_playlist_songs(songs, index=0):
    if index == len(songs):
        return
    print(songs[index])
    print_playlist_songs(songs, index + 1)

playlist = ["Kesariya", "Apna Bana Le", "Tum Hi Ho", "Heeriye", "Satranga"]

print_playlist_songs(playlist)




def count_unread_messages(group):
    total = group.get("count", 0)

    for sub in group.get("subgroups", []):
        total += count_unread_messages(sub)

    return total

messages = {
    "count": 10,
    "subgroups": [
        {
            "count": 5,
            "subgroups": [
                {"count": 2},
                {"count": 3}
            ]
        },
        {
            "count": 8
        }
    ]
}

print("Total Unread Messages:", count_unread_messages(messages))




x = "global"

def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"

    inner()
    print("Inside outer:", x)

outer()
print("Outside:", x)




def format_number_short(n):
    if n >= 1000000:
        return f"{n/1000000:.1f}M"
    elif n >= 1000:
        return f"{n/1000:.1f}K"
    else:
        return str(n)

print(format_number_short(1500))
print(format_number_short(1200000))
print(format_number_short(500))