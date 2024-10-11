import random

MAX_RANGE = 20
MIN_RANGE = 1
trial = 5
secret_no = random.randint(MIN_RANGE, MAX_RANGE)
attempts = 0

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between {MIN_RANGE} and {MAX_RANGE}. Can you guess it?")

while True:
    if attempts < trial:
        try:
            guess = int(input('Enter your guess: '))
            attempts += 1
            if guess < secret_no:
                print("Too low!")
            elif guess > secret_no:
                print('Too high!')
            else:
                print(f'Congratulations! You guessed the number {attempts} attempts')
                break
        except ValueError:
            print('Please enter a valid number.')
    else:
        print('You lose the game')
        break