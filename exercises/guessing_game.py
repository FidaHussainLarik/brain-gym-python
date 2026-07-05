import random 

secret_number = random.randint(1, 100)

while True:
    num = input("Guess the number: ")
    
    try:
        num = int(num)
    except:
        print("Invalid input , try again!⚠") # Other then number not accepted as input
        continue

    if num < secret_number:
        print("Too low!Try again. ")
    elif num > secret_number:
        print("Too high!Try again.")
    else:
        print("Congratulations! You guessed it!")
        break


