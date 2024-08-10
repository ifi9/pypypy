import random

number = random.randint(1, 50)
attempts = 5

while attempts > 0:
    guess = int(input("Guess the number (1-50): "))
    attempts -= 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")
        break

    if attempts == 0:
        print(f"Sorry, you're out of attempts. The number was {number}.")
    else:
        print(f"You have {attempts} attempts left.")
