win_counter = 0

for x in range(0, 6):
    check = input("did you win or lose the game?") #this code asks the user if they won or lost the game 6 times.

    if check == "win":
        win_counter = win_counter+1 #this code adds 1 point everytime the user responds wins a game.

if win_counter == (6) or win_counter == (5):
    print ("group 1") #If the user scores 6 or 5 wins, they are put in group 1.
if win_counter == (4) or win_counter == (3):
    print ("group 2") #If the user scores 4 or 3 wins, they are put in group 2.
if win_counter == (2) or win_counter == (1):
    print ("group 3") #If the user scores 2 or 1 wins, they are put in group 3.
if win_counter == (0):
    print ("eliminated") #If the user doesn't win any games, they are eliminated.