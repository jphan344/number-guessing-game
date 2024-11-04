import random

while True:
    print("Welcome to the Number Guessing Game! You have 3 tries to guess the correct number between 1 and 10.")
    number_to_guess = random.randint(1, 10)
    attempts = 0
    
    while attempts < 3:
        user_guess = int(input("Enter your guess: "))
        if user_guess == number_to_guess:
            print("Congratulations! You guessed the number correctly.")
            break
        else:
            if user_guess < number_to_guess:
                print("Sorry, that's too low.")
            else:
                print("Sorry, that's too high.")
            attempts += 1
            
    if attempts >= 3:
        print(f"Game over! The correct number was {number_to_guess}.")
    
    replay = input("Do you want to play again? (yes/no): ").strip().lower()
    if replay != 'yes':
        print("Thanks for playing!")
        break
