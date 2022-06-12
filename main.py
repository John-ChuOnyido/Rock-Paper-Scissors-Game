import random #importing the inbuilt python modules random
#using a while loop to set the code running while everything is true
while True:
    #making the code user friendly to collect the input from the user
    user_input = input("Enter a choice (R for rock, P for paper, S for scissors): ")
    possible_options = ["R", "P", "S"]#list storing the possible options for the computer
    CPU_player = random.choice(possible_options)#computer player making its choice from the possible options
    print(f"\nYou chose {user_input}, computer chose {CPU_player}.\n")
    """the main body of the code where the if, elif and else statements are used.
If the two players choose the same “character” it’s a tie, and the game repeats
Rock beats Scissors
Paper beats Rock
Scissors beats Paper"""
    if user_input == CPU_player:
        print(f"Both players selected {user_input}. It's a tie!")
    elif user_input == "R":
        if CPU_player == "S":
            print("Rock beats Scissors! You win!")
        else:
            print("Paper beats Rock! You lose.")
    elif user_input == "P":
        if CPU_player == "R":
            print("Paper beats Rock! You win!")
        else:
            print("Scissors beats Paper! You lose.")
    elif user_input == "S":
        if CPU_player == "P":
            print("Scissors beats Paper! You win!")
        else:
            print("Rock beats Scissors! You lose.")
    else:#error check when the enteringis incorrect
        print("Your entring is incorrect, please input again: ")
    """check if the user want to play again, if the user input is y then 
the game continue if its no the the game stops but if neither y nor n 
the it raise an error and the game stops"""
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        continue
    elif play_again.lower() == "n":
        break
    else:
        print("you just deviated, thank you for playing with me.")
        break
