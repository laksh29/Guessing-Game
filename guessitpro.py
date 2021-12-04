from random import randint
class Guess:
    def __init__(self):
        self.num = randint(0,9)
        self.guess = 0
        print(Guess.play(self.num,self.guess))
    def play(num,guess):
        count = 0
        while guess!= num:
            guess = int(input("Enter a number between 0-9: "))
            if guess > num: 
                print("Number guessed is high... Guess again!")
                count += 1
            elif guess < num: 
                print("Number guessed is low... guess again!")
                count += 1
            else: 
                print(f"YAYY... You guessed it right in {count} guess!")
                print(Guess.ask())
    def ask ():
        again = input("Do you want to play again?? {y/n}: ").lower()
        if again == 'y':
            return Guess()
        return("Thank you! play again!")
print(Guess())