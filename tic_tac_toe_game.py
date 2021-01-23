def build_grid(x, y, grid = None):
    str1 = ''
    str2_case1 = ''
    str3 = ''

    list_of_marks = []
    
    counter = 0
    
    grid_blank = []
    row_list = []
    
    for n in range(x):
        if n == 0:
            str1 += '    ---  '
            str3 += '    ' + str(n+1) + '  '
        else:
            str1 += '  ---  '
            str3 += '    ' + str(n+1) + '  '
    
    if grid:
        while counter < len(grid):
            str2_case2 = ''
            for n in range(x):
                if grid[counter][n] == 1:
                    str2_case2 += '|  O  |'
                elif grid[counter][n] == 2:
                    str2_case2 += '|  X  |'
                else:
                    str2_case2 += '|     |'
            list_of_marks.append(str2_case2)
            counter += 1
            
        print(' ' + str3)
        for i in range(len(grid)):
            print(str1)
            print(str(i+1) + ' ' + list_of_marks[i])
        print(str1)
                  
    else:
        for n in range(x):
            str2_case1 += '|     |'
            row_list.append(0)   
            
        print(' ' + str3)
        for i in range(y):
            print(str1)
            print(str(i+1) + ' ' + str2_case1)
            grid_blank += [row_list]
        print(str1)
    return grid_blank
    
def get_input(player, x, y):
    
    valid_choices_x = []
    valid_choices_y = []
    for i in range(x):
        valid_choices_x.append(str(i+1))
    for i in range(x):
        valid_choices_y.append(str(i+1))
    choice1 = ''
    choice2 = ''
    while choice1 not in valid_choices_x:
        print("\n" + player)
        print('Choose your row: ', valid_choices_x)
        choice1 = input('')
        if choice1 not in valid_choices_x:
            print('\nEnter a valid choice')
    
    while choice2 not in valid_choices_y:
        print('Choose your column: ', valid_choices_y)
        choice2 = input('')
        if choice2 not in valid_choices_y:
            print('\nEnter a valid choice')
        
    return int(choice1), int(choice2)
    
def go_again():
    print('\nDo you want to go again? y/n')
    opt = input('')
    valid_options = ['y', 'n']
    while opt not in valid_options:
        print('Enter a valid option')
        opt = input('')
    if opt == 'n':
        return False
    return True
    
def check_done(grid, win_count):
    y = len(grid)
    x = len(grid[0])
    win_1 = [1 for el in range(win_count)]
    win_2 = [2 for el in range(win_count)]
    sum_RL_1 = 0
    sum_LR_1 = 0
    sum_RL_2 = 0
    sum_LR_2 = 0
    const = x - 1
    
    for i in range(x):
        if grid[i] == win_1:
            return 1
        elif grid[i] == win_2:
            return 2
            
    for i in range(y):
        sum_1 = 0
        sum_2 = 0
        for j in range(x):
            if grid[j][i] == 1:
                sum_1 += 1
            elif grid[j][i] == 2:
                sum_2 += 2
        if sum_1 == win_count:
            return 1
        elif sum_2 == 2*win_count:
            return 2
            
    for i in range(y):
        if grid[i][i] == 1:
            sum_LR_1 += 1
        elif grid[i][i] == 2:
            sum_LR_2 += 2
        try:
            if grid[i][i+const] == 1:
                sum_RL_1 += 1
            elif grid[i][i+const] == 2:
                sum_RL_2 += 2
            const -= 2
        except IndexError:
            continue
    if sum_LR_1 == win_count or sum_RL_1 == win_count:
        return 1
    elif sum_LR_2 == 2*win_count or sum_RL_2 == 2*win_count:
        return 2
        
    check_zero = [True for num in grid if min(num) != 0]
    if len(check_zero) == y:
        return 0
            

def tic_tac_toe(x=3, y=3, won_count=3):
    
    done = False
    grid = build_grid(x, y)
    player1_wins = 0
    player2_wins = 0
    while not done:
        choice1_valid = False
        choice2_valid = False
        while not choice1_valid:
        
            choice1_y, choice1_x = get_input('Player 1', x, y)
            
            if grid[choice1_y-1][choice1_x-1] == 0:
                new_lst = grid[choice1_y-1].copy()
                new_lst[choice1_x-1] = 1
                grid[choice1_y-1] = new_lst
                choice1_valid = True
                build_grid(x, y, grid)
                if check_done(grid, won_count) == 1:
                    print('\nCongratulations Player 1!')
                    player1_wins += 1
                    done = go_again()
                    if done:
                        choice2_valid = True
                        done = False
                        grid = build_grid(x, y)
                    else:
                        print('Player 1: {0} wins!'.format(player1_wins))
                        print('Player 2: {0} wins!'.format(player2_wins))
                        return
                elif check_done(grid, won_count) == 2:
                    print('\nCongratulations Player 2!')
                    player2_wins += 1
                    done = go_again()
                    if done:
                        choice2_valid = True
                        done = False
                        grid = build_grid(x, y)
                    else:
                        print('Player 1: {0} wins!'.format(player1_wins))
                        print('Player 2: {0} wins!'.format(player2_wins))
                        return
                elif check_done(grid, won_count) == 0:
                    print('It is a draw!')
                    done = go_again()
                    if done:
                        choice2_valid = True
                        done = False
                        grid = build_grid(x, y)
                    else:
                        print('Player 1: {0} wins!'.format(player1_wins))
                        print('Player 2: {0} wins!'.format(player2_wins))
                        return
            else:
                print('\nThe space is occupied!')
                
            
        while not choice2_valid:
        
            choice2_y, choice2_x = get_input('Player 2', x, y)
            
            if grid[choice2_y-1][choice2_x-1] == 0:
                new_lst = grid[choice2_y-1].copy()
                new_lst[choice2_x-1] = 2
                grid[choice2_y-1] = new_lst
                choice2_valid = True
                build_grid(x, y, grid)
                if check_done(grid, won_count) == 1:
                    print('Congratulations Player 1!')
                    player1_wins += 1
                    done = go_again()
                    if done:
                        done = False
                        grid = build_grid(x, y)
                    else:
                        print('Player 1: {0} wins!'.format(player1_wins))
                        print('Player 2: {0} wins!'.format(player2_wins))
                        return
                elif check_done(grid, won_count) == 2:
                    print('Congratulations Player 2!')
                    player2_wins += 1
                    done = go_again()
                    if done:
                        done = False
                        grid = build_grid(x, y)
                    else:
                        print('Player 1: {0} wins!'.format(player1_wins))
                        print('Player 2: {0} wins!'.format(player2_wins))
                        return
                elif check_done(grid, won_count) == 0:
                    print('It is a draw!')
                    done = go_again()
                    if done:
                        done = False
                        grid = build_grid(x, y)
                    else:
                        print('Player 1: {0} wins!'.format(player1_wins))
                        print('Player 2: {0} wins!'.format(player2_wins))
                        return
            else:
                print('The space is occupied!')
                
        
        choice1_valid = False
        choice2_valid = False

tic_tac_toe() 