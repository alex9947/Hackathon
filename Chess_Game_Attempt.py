board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
# (0) Printing board
while True:
    print("Board")
    for a in range(0, 8):
        for j in range(0, 8):
            print(board[a][j], end=" ")
        print("")
    initial_column = int(input("Initial column: "))
    initial_row = int(input("Initial row: "))
    destination_column = int(input("Destination column: "))
    destination_row = int(input("Destination row: "))
    # (1) Check for piece in initial location
    pieceFound = False
    selectRow = board[initial_row - 1]
    if selectRow[initial_column - 1] == ".":
        print("There is no piece there.")
        break
    # (2) Remove piece from initial location
    else:
        selectChar = selectRow[initial_column - 1]
        selectRow[initial_column - 1] = ". "
        pieceFound = True
    # (3) Add piece to destination
    if pieceFound == True:
        selectRow = board[destination_row - 1]
        selectRow[destination_column - 1] = selectChar
