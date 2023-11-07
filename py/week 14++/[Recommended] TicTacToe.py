"""[Recommended] TicTacToe"""
def main(line1, line2, line3):
    """[Recommended] TicTacToe"""
    board = [line1, line2, line3]
    win = "DRAW"
    for i in range(3):
        if line1[i] == line2[i] == line3[i] and "-" != line1[i]:
            win = line1[i]
        elif board[i] == ["X", "X", "X"]:
            win = "X"
        elif board[i] == ["O", "O", "O"]:
            win = "O"
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        win = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        win = board[0][2]
    if win != "DRAW":
        win += " WIN"
    print(win)
main(list(input()), list(input()), list(input()))
