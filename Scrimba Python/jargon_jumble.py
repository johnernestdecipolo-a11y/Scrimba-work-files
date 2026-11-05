import random

words = ["blame", "crouch", "dragon", "mystique", "tardy"]

word = random.choice(words)

letters = list(word)
random.shuffle(letters)
scrambled = "".join(letters)

print(scrambled)