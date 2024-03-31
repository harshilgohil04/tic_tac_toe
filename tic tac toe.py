board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentplayer = "X"

def print_board():
    print(board[0] + "|", board[1] + "|", board[2])
    print("-------")
    print(board[3] + "|", board[4] + "|", board[5])
    print("-------")
    print(board[6] + "|", board[7] + "|", board[8])

print_board()

while True:
    inp = int(input("Enter a number between 1-9: "))
    if inp <= 9 and inp >= 1 and board[inp - 1] == "-":
        board[inp - 1] = currentplayer
        print_board()
        # Check for winning condition
        # Check rows
        if (board[0] == board[1] == board[2] != "-") or \
           (board[3] == board[4] == board[5] != "-") or \
           (board[6] == board[7] == board[8] != "-") or \
           (board[0] == board[3] == board[6] != "-") or \
           (board[1] == board[4] == board[7] != "-") or \
           (board[2] == board[5] == board[8] != "-") or \
           (board[0] == board[4] == board[8] != "-") or \
           (board[2] == board[4] == board[6] != "-") :

                print("Player", currentplayer, "wins!")
        
        # Switch player
        currentplayer = "O" if currentplayer == "X" else "X"
    else:
        print("Invalid input or cell already taken. Please try again.")