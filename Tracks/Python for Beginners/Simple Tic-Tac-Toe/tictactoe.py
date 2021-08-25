def print_grid(order):
    print("---------")
    print("|", order[0][0], order[0][1], order[0][2], "|")
    print("|", order[1][0], order[1][1], order[1][2], "|")
    print("|", order[2][0], order[2][1], order[2][2], "|")
    print("---------")


#  -----------------------------------------------------------------------------

def checkwins(xwin, ywin, order):
    for x in range(3):  # Runs for each row
        for a in "XO":
            if all(n == a for n in order[x]) == True:
                xwin += 1 if a == "X" else xwin
                ywin += 1 if a == "O" else ywin
            if all(order[y][x] == a for y in range(3)):
                xwin += 1 if a == "X" else xwin
                ywin += 1 if a == "O" else ywin

    for i in "XO":  # Checks diagnol
        if all(order[n][n] == i for n in range(3)):
            xwin += 1 if i == "X" else xwin
            ywin += 1 if i == "O" else ywin

        if all(order[n][2 - n] == i for n in range(3)):
            xwin += 1 if i == "X" else xwin
            ywin += 1 if i == "O" else ywin

    return xwin, ywin


#  -----------------------------------------------------------------------------

order = "_________"
order = [[order[x], order[x + 1], order[x + 2]] for x in range(0, 9, 3)]
turn = "X"
xwin = 0
ywin = 0

while True:

    print_grid(order)

    while True:
        coord = input("Enter the coordinates:").split()

        if len(coord) != 2:
            print("You should have two values")

        elif coord[0].isnumeric() == False or coord[1].isnumeric() == False:
            print("You should enter numbers!")

        elif coord[0] not in ("123") or coord[1] not in ("123"):
            print("Coordinates should be from 1 to 3!")

        elif order[int(coord[0]) - 1][int(coord[1]) - 1] in "XO":
            print("This cell is occupied! Choose another one!")

        else:
            break

    coord = [int(x) for x in coord]

    if turn == "X":
        order[coord[0] - 1][coord[1] - 1] = "X"
        turn = "O"
    elif turn == "O":
        order[coord[0] - 1][coord[1] - 1] = "O"
        turn = "X"

    xwin, ywin = checkwins(xwin, ywin, order)

    print(xwin, ywin)

    non_matrix_order = [x for x in range(0, 3) for x in order[x]]  # This gets the non matrix order of the order

    if xwin == 0 and ywin == 0 and all(x != "_" for x in non_matrix_order):
        print_grid(order)
        print("Draw")
        break
    elif xwin > ywin:
        print_grid(order)
        print("X wins")
        break
    elif ywin > xwin:
        print_grid(order)
        print("O wins")
        break






