import random
from hangmanlib import utils

words = utils.words
chosen_word = random.choice(words)
#print("Chosen word: ",chosen_word)

lifeline = 7
game_over = False
display = []

for i in range(len(chosen_word)):
    display += '_'
print("Fruit name:", display)
print("Length of word is:", len(display))
print("Lifeline is:", lifeline)

while not game_over:
    guess_letter = input("Guess a letter: ")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess_letter:
            display[position] = guess_letter
    if guess_letter not in chosen_word:
        lifeline -= 1
        if lifeline == 0:
            game_over = True
            print("You have Lost!")
    if '_' not in display:
        print("You won!!!")
        game_over = True

print(utils.stages[lifeline])
