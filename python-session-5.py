playlist_ids = [10,20,30,40,50]
print(playlist_ids)


playlist_ids.append(60)
playlist_ids.extend([70])
print(playlist_ids)


remove_song = playlist_ids.pop()
print(remove_song)
print(playlist_ids)


insta_filter = ("Los Angeles","Midnight","Grainy","Zoom Blur")
insta_filter[0]= "Paris"
print(insta_filter)