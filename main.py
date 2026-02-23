def tic_tac_toe(board):
    # Check all winings odds 
    if board[0][0] == board[0][1] == board[0][2]:return f'{board[0][0]} wins'
    elif board[1][0] == board[1][1] == board[1][2]:return f'{board[1][0]} wins'
    elif board[2][0] == board[2][1] == board[2][2]:return f'{board[2][0]} wins'
    elif board[0][0] == board[1][0] == board[2][0]:return f'{board[0][0]} wins'
    elif board[0][1] == board[1][1] == board[2][1]:return f'{board[0][1]} wins'
    elif board[0][2] == board[1][2] == board[2][2]:return f'{board[0][2]} wins'
    elif board[0][0] == board[1][1] == board[2][2]:return f'{board[0][0]} wins'
    elif board[0][2] == board[1][1] == board[2][0]:return f'{board[0][2]} wins'
    # if there is no winner
    else: return "Draw"

if __name__ == '__main__':
    print(tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]))
    print('============')
    print(tic_tac_toe([["O", "O", "X"], ["X", "O", "X"], ["O", "X", "X"]]))
    print('============')
    print(tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]))
    print('============')
    print(tic_tac_toe([["X", "X", "O"], ["X", "O", "O"], ["O", "O", "X"]]))
    print('============')
    print(tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]]))
    print('============')
    print(tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]))
    print('============')