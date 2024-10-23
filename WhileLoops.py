## Guessing game
## System sets a with random.randint
import random 
def main():
    x = 1 
    hidden_num = random.randint(1, 100)
    # generates integer value for hidden_num using func from random library
    print(hidden_num)
    while x == 1: 
        guess = int(input("Please guess an integer between 1 and 100: "))
        if guess == hidden_num:
            x = x - 1
        # very little logic needed for this while loop.
        else:
            print("Wrong, guess again!")
    print(f"Congratulations; your guess of {guess} equalled the number in my head, {guess}")
main()