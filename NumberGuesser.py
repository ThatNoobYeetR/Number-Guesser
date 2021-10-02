import random
n = random.randint(0, 100)
print("Guess the number.")




while True:
    numberguess = int(input())


    if numberguess > n:
        print("Smaller.")


    if numberguess < n:
        print("Bigger.")
    
    if numberguess == n:
        print("Correct! You win!")