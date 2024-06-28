# Function to check if two strings are similar (case-insensitive)
def similar(a, b):
    return a.lower() == b.lower()

print("Welcome to the Patch Quiz!")

# Question 1
age = input("1. How old is Patch? ")
if age == "4":
    print("Good Job! Now let's see if you really love him....")
else:
    print("Hmm, that's not correct. Let's continue anyway.")

# Question 2
dinner_time = input("2. What time does he have dinner (don't type pm)? ")
if dinner_time == "8:30":
    print("Nice work")
elif dinner_time == "8":
    print("Maybe wait a little longer hun, seriously.")
elif dinner_time == "9":
    print("Why do you wait so long to feed him. He should eat earlier.")
else:
    print("That doesn't seem right.")

# Question 3
birds = input("3. What type of birds does Patch like to hunt? ")
if similar(birds, "Geese") or similar(birds, "Ducks") or similar(birds, "Gooses"):
    print("You're right, you love your dog.")
else:
    print("Hmmm, seriously.")

print("Hope you enjoyed your game.")