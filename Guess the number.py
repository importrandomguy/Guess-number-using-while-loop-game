import random
number=random.randrange(1,10)#you can increase/decrease the range 
while True:
    guess=int(input("Enter a of your wish: "))
    if guess<number:
        print("The number you guessed is lesser!")
        print("Try again!")
    elif guess>number:
        print("The number you guessed is greater!")
        print("Try again!")
    elif guess==number:
        print("Congratulations! you guessed the correct number")
        break
