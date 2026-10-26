# PART 1 - USER DETAILS
name = input("What is your name? ")
mood = input("How is your mood today? (happy/sad/tired/stressed/excited): ")
energy = int(input("Rate your energy from 1 to 10: "))
mood = mood.lower()

# PART 2 - ENERGY CHECK
print("\n--- YOUR ENERGY ---")
if energy <= 3:
    print("Your energy is low today.")
    print("Try to take a break and get some rest.")
elif energy <= 6:
    print("Your energy is in the middle.")
    print("Start with a small task and take breaks.")
else:
    print("Your energy is high today!")
    print("You could use it for something you enjoy.")

# PART 3 - MOOD ADVICE AND ACTIVITY
print("\n--- MOOD ADVICE ---")
if mood == "happy":
    advice = "Keep enjoying your day!"
    activity = "Listen to your favourite songs or spend time with friends."
elif mood == "sad":
    advice = "Give yourself time. You do not have to feel okay all the time."
    activity = "Talk to someone you trust or do something comforting."
elif mood == "tired":
    advice = "You might need a little rest."
    activity = "Take a break, drink some water, or get some sleep."
elif mood == "stressed":
    advice = "Take things one step at a time."
    activity = "Write down your tasks and start with the easiest one."
elif mood == "excited":
    advice = "Make the most of your excitement!"
    activity = "Try a creative activity or start something you have been planning."
else:
    advice = "It is okay if you cannot describe your mood."
    activity = "Take a little time for yourself and do something you enjoy."
print("Advice:", advice)
print("Suggested Activity:", activity)

# PART 4 - CHECK YOUR ENERGY
if energy >= 7 and mood != "tired":
    print("You might have enough energy to try your suggested activity.")
else:
    print("Take your time. You can do your activity whenever you feel ready.")

# PART 5 - DATE AND TIME
import datetime
today = datetime.datetime.now()

# PART 6 - DAILY REPORT
print("\n================================")
print("        DAILY MOOD REPORT")
print("================================")
print("Name:", name)
print("Today's Mood:", mood.capitalize())
print("Energy Level:", energy, "/10")
print("Date and Time:", today)
print("--------------------------------")
print("Today's Advice:", advice)
print("Today's Activity:", activity)
print("================================")
