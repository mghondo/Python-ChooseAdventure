import random

# ASCII art for rock, paper, scissors
rock = """
    _    
   | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\\
"""

paper = """
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
"""

scissors = """
     _                        
     (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \\
|___/\___|_|___/___/\___/|_|  |___/
"""

# Game logic
def play_game():
    choices = [rock, paper, scissors]
    choice_names = ["Rock", "Paper", "Scissors"]
    
    print("Welcome to Rock Paper Scissors!")
    
    while True:
        print("\nMake your choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        
        player_choice = input("Enter the number of your choice (1-3): ")
        
        if player_choice not in ["1", "2", "3"]:
            print("Invalid choice. Please try again.")
            continue
        
        player_choice = int(player_choice) - 1
        computer_choice = random.randint(0, 2)
        
        print("\nYou chose:")
        print(choices[player_choice])
        print(f"({choice_names[player_choice]})")
        
        print("\nComputer chose:")
        print(choices[computer_choice])
        print(f"({choice_names[computer_choice]})")
        
        if player_choice == computer_choice:
            print("\nIt's a tie!")
        elif (player_choice == 0 and computer_choice == 2) or \
             (player_choice == 1 and computer_choice == 0) or \
             (player_choice == 2 and computer_choice == 1):
            print("\nYou win!")
        else:
            print("\nComputer wins!")
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "y3":
            break
    
    print("Thanks for playing!")

# Run the game
play_game()