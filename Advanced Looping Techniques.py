#Task 1

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
sublist_genres = genres[1:4]

for genres in sublist_genres:
    print(genres)


#Task 2

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
genres_and_music = []

for genre in genres:
    genres_and_music.append(genre + " Music")

print(genres_and_music)


#Task 3

for number in range(10, 0, -1):
    print(number)
print("The beat drops now!")