#Task 1

import random

items = ["Headphones", "Laptop", "Phone", "Wallet", "Watch"]
selected_item = random.choice(items)
guess = input("Guess the selected item from the list: ")

if guess == selected_item:
    print(f"Nice job! {selected_item} is correct!")
else:
    print(f"Uh oh, not quite! The selected item was {selected_item}:(")