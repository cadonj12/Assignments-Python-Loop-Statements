#Task 1

import random

different_moods = ["Happy", "Sad", "Energetic", "Calm"]
different_days = ["Monday", "Tuesday", "Wednesday", "Thursday",
"Friday", "Saturday", "Sunday"]

for i in range(len(different_days)):
    mood = random.choice(different_moods)
    print(f"On {different_days[i]}, I was feeling {mood}.")