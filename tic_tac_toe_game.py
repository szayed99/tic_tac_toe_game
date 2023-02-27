import numpy as np
def draw_grid(game):
    valid_choices = {}
    counter = 0
    for i in range(len(game)):
        current_row = ""
        for j in range(len(game)):
            current_pos = game[i][j]
            if current_pos == 0:
                current_row += " " + str(counter) + " |"
                valid_choices[str(counter)] = [i, j]
            elif current_pos == 1:
                current_row += " O |"
            elif current_pos == 2:
                current_row += " X |"
            counter += 1
        current_row = current_row[:-2]
        print(current_row)
        if i != 2:
            print("――――――――――")
    return valid_choices
def check_winner(game):
    for i in range(len(game)): # checks all directions
        if len(game[i][game[i] == 1]) == 3 or len(game[:, i][game[:, i] == 1]) == 3 or len(game.diagonal()[game.diagonal() == 1]) == 3 or len(game[::-1].diagonal()[::-1][game[::-1].diagonal()[::-1] == 1]) == 3: 
            return 1
        elif len(game[i][game[i] == 2]) == 3 or len(game[:, i][game[:, i] == 2]) == 3 or len(game.diagonal()[game.diagonal() == 2]) == 3 or len(game[::-1].diagonal()[::-1][game[::-1].diagonal()[::-1] == 2]) == 3: 
            return 2
    if game[0].sum() + game[1].sum() + game[2].sum() == 13:
        return 3
def make_move(piece, game): #piece = 1 for O, 2 for X
    done = False
    while not done:
        valid_choices = draw_grid(game)
        choice = input("\nPick an empty square number: ")
        if choice in valid_choices.keys():
            game[valid_choices[choice][0], valid_choices[choice][1]] = piece
            print("\n")
            done = True
        else:
            print("Pick a valid number\n")
    return game
def play(game):
    done = False
    while not done:
        game = make_move(1, game)
        if check_winner(game) == 1:
            draw_grid(game)
            print("\nO Won!")
            return
        elif check_winner(game) == 3:
            draw_grid(game)
            print("\nDraw!")
            return
        game = make_move(2, game)
        if check_winner(game) == 2:
            draw_grid(game)
            print("\nX Won!")
            return

game = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])       
play(game)
