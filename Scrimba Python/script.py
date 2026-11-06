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

inventory = [
    ("notebooks", 42),
    ("pens", 130),
    ("staplers", 8),
]

item, quantity = inventory[0]
print(f"{item}: {quantity} in stock")

item, quantity = inventory[1]
print(f"{item}: {quantity} in stock")

item, quantity = inventory[2]
print(f"{item}: {quantity} in stock")