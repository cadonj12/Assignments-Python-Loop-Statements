#Task 1

iterations = 0

while True:
    print("Inside loop.")

    iterations += 1

    if iterations >= 5:
        break

#Task 2

iterations = 0
condition_met = False

while not condition_met:
    print("Inside loop.")

    iterations += 1

    if iterations >= 5:
        condition_met = True