## My First Game ##
import random

print("Hello, my name is The Guess Master 9000.")
print("What is your name mortal?")
name = input()

print("well, " + name + ", am thinking of a number between 1 and 20")
secrectNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print("take a guess.")
    guess = int(input())

    if guess < secrectNumber:
        print("guess is too low.")
    elif guess > secrectNumber:
        print("guess is too high.")
    else:
        break #This condition is for the correct guess!

if guess == secrectNumber:
    print("Good Job, " + name + "!You guessed my number in " + str(guessesTaken) + " guesses!")
else:
    print("Nope. The number I was Thinking of was " + str(secrectNumber))
    
