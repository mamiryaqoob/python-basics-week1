secret = 4
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number: "))
    
    if guess == secret:
        print("You won!")
        break
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("Game over! The number was", secret)