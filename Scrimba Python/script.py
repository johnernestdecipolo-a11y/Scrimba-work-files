# code = "FLASH50"

# promo_code = input("Enter the promo code: ")
# print(code == promo_code)
# print(code != promo_code) 

# unread_message = 0
# age = 25
# cart_total = 45
# tickets_left = 8

# print(f"Has unread messages (more than 0): {unread_message > 0}")
# print(f"Old enough to rent a car (25 or older): {age >= 25}")
# print(f"Under the $50 free-shipping minimum: {cart_total < 50}")
# print(f"Sold out(0 or fewer tickets left): {tickets_left <= 0}")

# decibels = 90

# if decibels > 89:
#     print("Warning: Loud Environment!")

# score = 60

# student_score = int(input("What's your score?"))

# if student_score >= score:
#     print("You passed!")
# else:
#     print("You failed!")

# signal_bars = int(input("Type your signal strength (0-5), customers get a discount if wifi bar is below 5!: " ))

# if signal_bars == 0:
#     print("50% off, sorry about the Wi-Fi!")
# elif signal_bars <=2:
#     print("25% off")
# elif signal_bars <=4:
#     print("10% off")
# elif signal_bars == 5:
#     print("Full bars, no discount today!")
# else:
#     print("Type a valid number for your discount!")

# promo_code = "spring25"
# full_name = "jamie rivera"
# email = "  Jamie@Example.COM"
# display_name = "   the ROCK   "

# print(promo_code.upper())
# print(full_name.title())

# clean_email = email.strip().lower()
# print(clean_email)

# clean_display_name = display_name.strip().title()
# print(clean_display_name)

# import random

# words = ["apple", "orange", "banana"]

# word = random.choice(words)
# print(word)

# letters = list(word)
# random.shuffle(letters)
# scrambled_word = "".join(letters)

# print(f"Scrambled: {scrambled_word}")

# guess = (input("Guess the word (or type 'skip' to skip)").strip().lower())

# if guess == "skip":
#     print(f"Skipped! The word was '{word}'.")
# elif guess == word: 
#     print("Correct!")
# elif guess == "":
#     print("Type in your word")
# else: 
#     print(f"Sorry, the word was: {word}")

# inventory = [
#     ("notebooks", 42),
#     ("pens", 130),
#     ("staplers", 8),
# ]

# item, quantity = inventory[0]
# print(f"{item}: {quantity} in stock")

# item, quantity = inventory[1]
# print(f"{item}: {quantity} in stock")

# item, quantity = inventory[2]
# print(f"{item}: {quantity} in stock")

import random

word_bank = [
    ("standup", "Every morning, our fifteen-minute ____ meeting lasts until lunch."),
    ("syntax", "One missing bracket, and Python hits me with a ____ error."),
    ("debug", "I spent four hours trying to ____ my code. Turns out I was missing a comma."),
    ("deploy", "It's Friday at 5pm, definitely the best time to ____ new code."),
    ("bandwidth", "Sorry boss, I can't take on more work. I just don't have the ____."),
    ("meeting", "That ninety-minute ____ could have been an email."),
    ("deadline", "Of course we'll hit the ____, no problem! Well, within a couple of days. Maybe a week."),
    ("backup", "We finally made a ____ of everything, the day after the laptop died."),
    ("server", "I'm getting a 500 error, which means the ____ is down again."),
    ("prototype", "It's just an early ____, so please ignore that clicking anywhere crashes it."),
]

ROUNDS = 5
round_num = 1
score = 0
score_final = 5

used = []

while round_num <= ROUNDS: 
     
    word, hint = random.choice(word_bank)

    while (word, hint) in used:
        word, hint = random.choice(word_bank)

    used.append((word,hint))

    letters = list(word)
    random.shuffle(letters)
    scrambled_word = "".join(letters).upper()


    print(f"Round {round_num} of {ROUNDS}:")
    print(f"Total score:{score}/{score_final}")
    print(f"Scrambled: {scrambled_word}")

    guess = input("Guess the word (or type 'hint' / 'skip' / 'quit): ").strip().lower()
   

    if guess == "hint":
        print()
        print(f"Hint: {hint}")
        print()
        guess = input("Your guess (or 'skip'): ").strip().lower()

    if guess == "quit":
        print(f"Thanks for playing!")
        break
    if guess == "skip":
        print(f"Skipped! The word was '{word}'.")
    elif guess == word:
        score += 1
        print("✅ Correct!")
    elif guess == "":
        print("Please type your answer.")
    else:
        print(f"❌ Sorry, the word was '{word}'.")
    
    round_num += 1

print(f"Final Score: {score}/{score_final}")

if score == 5:
    print(f"A score of {score}:Flawless! All tests passing, zero bugs.")
elif score == 4:
    print(f"Near perfect, only one failing test!")
elif score == 3:
    print(f"Good effort! The code runs, and that's what counts.")
else:
    print("Have you tried turning it off and on again?")

# count = 2

# while count <= 5:
#     print(count)
#     count += 1

# PASSENGERS = 5
# passenger_num = 1

# while passenger_num <= PASSENGERS:
#     print(f"Printing boarding pass {passenger_num} of {PASSENGERS}")
#     passenger_num += 1

# lobby = []

# lobby.append("Xena")
# lobby.append("Thor")
# lobby.append("Merlin")
# lobby.append("Ripley")
# print(lobby)

# entrants = ["Amara", "Diego", "Priya", "Leo", "Sofia", "Kwame"]
# winners = ["Diego", "Sofia"]

# import random

# pick = random.choice(entrants)

# while pick in winners:
#     pick = random.choice(entrants)

# winners.append(entrants)
# print(f"Winner: {pick}")
