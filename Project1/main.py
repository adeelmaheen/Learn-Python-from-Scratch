# we all have played snake, water gun game in our chilhood. if you haven't goole the rules of this game and write a python program capable of playing this game with the user.

import random

# Define the possible moves
choices = ["Snake", "Water", "Gun"]

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Snake" and computer_choice == "Water") or \
         (player_choice == "Water" and computer_choice == "Gun") or \
         (player_choice == "Gun" and computer_choice == "Snake"):
        return "You win!"
    else:
        return "Computer wins!"

# Main function to play the game
def play_game():
    print("               Welcome to Snake-Water-Gun Game!                            ")
    print("Rules: Snake vs Water -> Snake wins | Water vs Gun -> Water wins | Gun vs Snake -> Gun wins")
    
    while True:
        # Get player choice
        player_choice = input("Choose 'Snake', 'Water', or 'Gun' (or type 'quit' to end): ").capitalize()
        
        if player_choice == 'Quit':
            print("Thanks for playing! Goodbye!")
            break
        
        if player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        # Get computer choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine and display the winner
        result = determine_winner(player_choice, computer_choice)
        print(result)
        print()

# Start the game
play_game()


