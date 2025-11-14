def print_board(b):
    print()
    print(b[0]+"|"+b[1]+"|"+b[2])
    print("-+-+-")
    print(b[3]+"|"+b[4]+"|"+b[5])
    print("-+-+-")
    print(b[6]+"|"+b[7]+"|"+b[8])
    print()

def check_win(b, p):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]
    for x,y,z in win:
        if b[x] == b[y] == b[z] == p:
            return True
    return False

def empty_spots(b):
    return [i for i in range(9) if b[i] == " "]

def minimax(b, is_max):
    if check_win(b, "O"):
        return 1
    if check_win(b, "X"):
        return -1
    if " " not in b:
        return 0

    if is_max:
        best = -10
        for i in empty_spots(b):
            b[i] = "O"
            val = minimax(b, False)
            b[i] = " "
            best = max(best, val)
        return best
    else:
        best = 10
        for i in empty_spots(b):
            b[i] = "X"
            val = minimax(b, True)
            b[i] = " "
            best = min(best, val)
        return best

def best_move(b):
    move = -1
    best_score = -10
    for i in empty_spots(b):
        b[i] = "O"
        score = minimax(b, False)
        b[i] = " "
        if score > best_score:
            best_score = score
            move = i
    return move

board = [" "] * 9
print("Tic-Tac-Toe: You = X, AI = O")

while True:
    print_board(board)
    try:
        move = int(input("Choose (1-9): ")) - 1
        if board[move] == " ":
            board[move] = "X"
        else:
            print("Taken!")
            continue
    except:
        print("Invalid!")
        continue

    if check_win(board, "X"):
        print_board(board)
        print("You win!")
        break
    if " " not in board:
        print_board(board)
        print("Draw!")
        break

    ai = best_move(board)
    board[ai] = "O"

    if check_win(board, "O"):
        print_board(board)
        print("AI wins!")
        break
    if " " not in board:
        print_board(board)
        print("Draw!")
        break
