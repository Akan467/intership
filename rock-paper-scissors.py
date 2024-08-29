import random

def play_game():
    # Define the possible choices
    choices = ["rock", "paper", "scissors"]
    
    # Get the user's choice
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    # Validate user input
    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return
    
    # Generate the computer's choice
    computer_choice = random.choice(choices)
    
    # Print both choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
        
# Play the game
play_game()
