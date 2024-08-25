import random

options = ("rock", "paper", "scissors")
playing = True

while playing:

    computer = random.choice(options)
    player = input("Enter a choice (rock, paper, scissors): ")

    print("Player: " + player)
    print("Computer: " + computer)

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if input("Play again? (y/n): ").lower() != "y":
        playing = False

print("Thanks for playing!")