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

# import random

# def scrambled_word():

#     word = input("Enter a word: ")
#     letters = list(word)
#     random.shuffle(letters)
#     scrambled = "".join(letters)
#     return scrambled

# result = scrambled_word()
# print(result)

# import math

# def slices_needed(guests):
#     return guests * 2

# def pizzas_needed(slices):
#     return math.ceil(slices / 8)

# slices = slices_needed(10)
# pizzas = pizzas_needed(slices)
# print(pizzas)

# import math

# def room_area(length, width):
#     return length * width

# def add_tax(price):
#     return price * 1.08

# def full_name(first, last):
#     return first + " " + last

# square_feet = room_area(12, 10)
# total = add_tax(50)
# greeting = full_name("Mike", "Reed")

# print(f"The room is {square_feet}square feet.")
# print(f"With tax, that comes to ${total}.")
# print(f"Welcome, {greeting}!")

# nominees = ["PixelPal", "TaskTanic", "SnackMap", "MoodTunes"]

# for nominee in nominees:
#     print(f"Nominated for Best New App: {nominee}")

# print("And those are your nominees!")

# lineup = [
#     ("The Wailers", "reggae", 45),
#     ("Daft Punk", "electronic", 90),
#     ("Adele", "pop", 60),
#     ("Metallica", "metal", 100),
# ]

# for artist in lineup:
#     band, genre, minutes = artist

#     if minutes >= 90:
#         print(f"{band} ({genre}) plays a long set: {minutes} minutes")
#     else:
#         print(f"{band} ({genre}) plays {minutes} minutes")

queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]
def show_queue(queue):
    print()
    print(f"Current Queue: ")
    print() 
    for i, singer in enumerate(queue):
        name, song = singer
        print(f"{i + 1}. {name} - {song}")
    print()
print("Options:  add / next / remove / quit")

def prompt_for_singer():
    singer = input("Singer name: ").strip().title()
    song = input("Song name:").strip().title()
    return singer, song
def add_singer(queue):
    singer, song = prompt_for_singer()
    queue.append((singer, song))
    print(f"{singer} - {song} has been added to the list! ")
def next_singer(queue):
    next = queue.pop(0)
    print(next)
    print(queue)
def remove_singer(queue):
    singer_to_remove = input("Who do you want to remove? ").strip().title()
    for singer, song in queue:
        if singer == singer_to_remove:
            queue.remove((singer, song))
            print(f"{singer} - {song} has been removed from queue.")
            return
    print(f"There's no one named {singer_to_remove} in the queue.")
def run_app(queue):
    print("=" * 44)
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("=" * 44)

    is_running = True

    while is_running:
        show_queue(queue)
        print()
        print("Options: add / next / remove / quit")
        command = input("> ")

        if command == "quit":
            is_running = False
            print("The queue is closed. Good night!")

        elif command == "add":
            add_singer(queue)

        elif command == "next":
            next_singer(queue)

        elif command == "remove":
            remove_singer(queue)

        else: 
            print(f"Sorry, I don't know the command '{command}'")

run_app(queue)

