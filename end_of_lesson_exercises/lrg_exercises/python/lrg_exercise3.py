import random
secret_number = random.randint(1, 10)
done = "no"
valid = True

def play_game():
    attempts = 5
    print("\nPlease guess the number between 1 and 10. You will have %i attempts." %attempts)
    valid = True
    while valid:
        while True:
            try:
                guess = int(input("Please enter the number that you believe is the answer:  "))
                break
            except ValueError:
                print("Sorry!! You did not submit a number!")
        if attempts > 1 and attempts < 6:
            if guess == secret_number:
                print("You win!!")
                break
            elif guess < secret_number:
                print("%i is too low. Try a little higher." % guess)
                attempts -= 1
                print("You now have %i guesses left." %attempts)
            else:
                print("%i is too high. Why don't you lower it a little bit." % guess)
                attempts -= 1
                print("You now have %i guesses left." %attempts)
        else:
            print("Sorry you lost.")
            valid = False
def once_more():
    valid = True
    while valid:
        play_again = input("Would you like to play again? Yes(y) or No(n):  ")
        if play_again == "Yes" or play_again == "y":
            play_game()
        elif play_again == "No" or play_again == "n":
            valid = False
        else:
            print("Please enter Yes(y) or No(n).")

while valid:
    play_game()
    once_more()
    valid = False
print("Goodbye. Have a Great Day!")
