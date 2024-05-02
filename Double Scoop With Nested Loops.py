#Task 1

import random

different_moods = ["Happy", "Sad", "Energetic", "Calm"]
different_days = ["Monday", "Tuesday", "Wednesday", "Thursday",
"Friday", "Saturday", "Sunday"]
time_of_day = ["Morning", "Afternoon", "Evening"]

for day_index in range(len(different_days)):
    day = different_days[day_index]
    for time_index in range(len(time_of_day)):
        time = time_of_day[time_index]
        mood = random.choice(different_moods)

        print(f"On {day} {time} I was feeling {mood}.")