# CodeAplha Internship [ Python Programming Task ]
# Task -1
# Hangman Game:
"""Create a simple text-based Hangman game where the player
gusses a word one letter at a time"""

#Solution of Task-1

import random
create_list= ["code","alpha","yellow", "green","blue"]
word=random.choice(create_list)
display=["_"]*len(word)
guess_letter=set()
tries=6
print ("HELLO Player! welcome to the hangman game")
while tries > 0:
    num = input("enter a letter: ")
    if num in guess_letter:
        print ("you already guessed that letter")
        continue
    guess_letter.add(num)
    if num in word:
        for i in range(len(word)):
            if word[i] == num:
                display[i] = num
    else:
        print("Wrong guess!")
        tries -= 1
    print("Tries left:", tries)
    print("Word:", " ".join(display))
    if "_" not in display:
        print("You win the game! The word was:", word)
if "_" in display:
    print(" You lost the game. The word was:", word)


#Summary
""""This Python program is a simple Hangman game. It:
1.Randomly picks a word from a list using the random module.
2.Uses a list (display) to show correct guesses and blanks (_).
3.Tracks guessed letters using a set to avoid repeated guesses.
4.Gives the player 6 tries to guess the word.
5.Uses a while loop to continue the game until the player wins or runs out of tries.
6.Uses input() to take letter guesses and if conditions to check if guesses are correct and else.
7.In the end, it prints whether the player won or lost and reveals the word."""