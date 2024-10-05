import random

from constants import ENTER_CHOICE, INVALID_CHOICE, TIE_MESSAGE, USER_WIN_MESSAGE, COMPUTER_WIN_MESSAGE, \
    GOODBYE_MESSAGE, USER_CHOISE, COMPUTER_CHOISE


def get_user_choice():
    """
    Prompt the user to enter their choice (rock, paper, scissors, or exit).
    Validates the input and keeps asking until a valid choice is made.

    Returns:
    str: The user's choice, converted to lowercase.
    """
    choice = input(ENTER_CHOICE).lower()
    while choice not in ['rock', 'paper', 'scissors', 'exit']:
        print(INVALID_CHOICE)
        choice = input(ENTER_CHOICE).lower()
    return choice


def get_computer_choice():
    """
    Randomly select and return the computer's choice (rock, paper, or scissors).

    Returns:
    str: The computer's randomly selected choice.
    """
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    """
    Determine the winner based on the user and computer's choices.

    Parameters:
    user_choice (str): The user's choice (rock, paper, or scissors).
    computer_choice (str): The computer's choice (rock, paper, or scissors).

    Returns:
    str: The result of the game (user wins, computer wins, or a tie).
    """
    if user_choice == computer_choice:
        return TIE_MESSAGE
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return USER_WIN_MESSAGE
    else:
        return COMPUTER_WIN_MESSAGE


def play_game():
    """
    Main function to run the Rock-Paper-Scissors game.
    Continuously prompts the user to play until 'exit' is chosen.
    """
    while True:
        user_choice = get_user_choice()
        if user_choice == 'exit':
            print(GOODBYE_MESSAGE)
            break

        computer_choice = get_computer_choice()

        print(f"\n{USER_CHOISE}: {user_choice}")
        print(f"{COMPUTER_CHOISE}: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"\n{result}\n")


# Run the game
if __name__ == "__main__":
    play_game()
