# import random 

# def announce_coffee_run():
#     print("I am headed to the coffee shop! Who wants a latte?")
# def quantity_of_latte():
#     amount = int(input("How many lattes do you need?"))
#     return amount
# def calc_coffee_total():
#     latte = quantity_of_latte()
#     latte_price = 5
#     print(f"{latte} lattes comes to $ {latte * latte_price}")

# def say_welcome():
#     print("You're welcome!")
#     print("You're welcome!")

# def coffee_run():
#     announce_coffee_run()
#     calc_coffee_total()
#     say_welcome()
#     say_welcome()
#     say_welcome()

# coffee_run()

# def add_numbers(num1, num2):
#     print(num1 + num2)

# add_numbers(2, 3)
# add_numbers(5, 8)

import random

def scrambled_word():

    word = input("Enter a word: ")
    letters = list(word)
    random.shuffle(letters)
    scrambled = "".join(letters)
    return scrambled

result = scrambled_word()
print(result)