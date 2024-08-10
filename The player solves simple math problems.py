import random

score = 0

for i in range(5):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 + num2

    guess = int(input(f"What is {num1} + {num2}? "))

    if guess == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {answer}.")

print(f"Your score: {score}/5")
