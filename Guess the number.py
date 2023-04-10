number=10
while True:
    guess=int(input("Enter a of your wish: "))
    if guess<10:
        print("The number you guessed is lesser!")
        print("Try again!")
    elif guess>10:
        print("The number you guessed is greater!")
        print("Try again!")
    elif guess==10:
        print("Congratulations! you guessed the correct number")
        break