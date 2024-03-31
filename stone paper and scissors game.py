import random
from tkinter import *
from tkinter import messagebox

def get_player_choice():
    choice = player_choice_var.get()
    while choice not in ['rock', 'paper', 'scissors']:
        messagebox.showerror("Error", "Invalid choice. Please choose rock, paper, or scissors.")
        choice = player_choice_var.get()
    return choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose."

def play_against_computer():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    messagebox.showinfo("Result", f"You chose {player_choice}. The computer chose {computer_choice}. {result}")

def play_against_player():
    player1_choice = get_player_choice()
    player2_choice = get_player_choice()
    result = determine_winner(player1_choice, player2_choice)
    messagebox.showinfo("Result", f"Player 1 chose {player1_choice}. Player 2 chose {player2_choice}. {result}")

def play_game():
    choice = game_mode_var.get()
    if choice == 'play against computer':
        play_against_computer()
    elif choice == 'play against player':
        play_against_player()
    else:
        root.quit()

root = Tk()
root.title("Stone Paper Scissors")

game_mode_var = StringVar(root)
game_mode_var.set('play against computer')

player_choice_var = StringVar(root)
player_choice_var.set('rock')

game_mode_menu = OptionMenu(root, game_mode_var, 'play against computer', 'play against player', 'quit')
game_mode_menu.pack()

player_choice_menu = OptionMenu(root, player_choice_var, 'rock', 'paper', 'scissors')
player_choice_menu.pack()

play_button = Button(root, text="Play", command=play_game)
play_button.pack()

root.mainloop()