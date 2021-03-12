import random
print("Welcome!")
def guess(x):
    random_number = random.randint(1,x)
    guessed = 0
    while guessed != random_number :
        guessed = int(input(f'Enter a number between 1 and {x}: '))
        if guessed < random_number:
            print("Guess is too low. Try again!")
        elif guessed > random_number:
            print("Guess is too high. Try again!")
        else:
            print("You got it!")

guess(100)