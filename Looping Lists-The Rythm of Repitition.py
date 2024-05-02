#Task 1

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
track_number = 1

for genre in genres:
    print(f"Track {track_number}: {genre} is playing.")
    track_number += 1
    
    
#Task 2

track_number = 0

while track_number < len(genres):
         track_number += 1
         genre = genres[track_number - 1]
      
         print(f"Track {track_number}: {genre} is playing.")
         if genre == 'Hip-hop':
                break


#Task 3

for track_number in range(len(genres)):
       genre = genres[track_number]
       if genre == 'Classical':
              continue
       print(f"Track {track_number + 1}: Our light show is ready for {genre}!")
