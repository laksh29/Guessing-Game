def roll():
    from random import randint 
    num = randint(0,10)
    guess = 0
    play(guess,num)
def play(guess,num):
    while guess!=num:
        guess = int(input("\nEnter a number between 0 to 9: "))
        if guess >num:
            print("Number guessed is high... Guess again: ")
        elif guess < num:
            print("Number guessed is low... Guess again: ")
        else:
            print("Yayyyy... You guessed it right!")
            ask()
def ask():
    again  = input("\nDo you want to play again?? (y/n): ").lower()
    if again == 'y':
        return roll()
    else:
        print("Thank you! Play again!")
roll()