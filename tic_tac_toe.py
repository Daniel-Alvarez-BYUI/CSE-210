from collections import deque
from turtle import position
turn = deque(["0","X"])
board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "],
]
def show_board():
    print("")
    for row in board:
        print(row)

def update_board(pos, player):
    board[pos[0]][pos[1]] = player

def change_turn():
    turn.rotate()
    return turn[0]

def process_position(position):
    row,col = position.split(",")
    return [int(row)-1 ,int(col)-1]

def correct_position(pos):
    if 0 <= pos[0] <= 2 and 0 <=pos[1] <= 2:
        if board[pos[0]][pos[1]] == " ":
            return True
    return False

def win(j):
    #compare rows of the board
    if board[0] == [j,j,j] or board[1] == [j,j,j] or board[2] == [j,j,j]:
        return True
    #compare columns of the board   
    elif board[0][0] == j and board[1][0] == j and board[2][0] == j:
        return True
    elif board[0][1] == j and board[1][1] == j and board[2][1] == j:
        return True
    elif board[0][2] == j and board[1][2] == j and board[2][2] == j:
        return True
    #compare rows of the board
    elif board[0][0] == j and board[1][1] == j and board[2][2] == j:
        return True
    elif board[0][2] == j and board[1][1] == j and board[2][0] == j:
        return True
    return False
def main():
    show_board()
    player = change_turn()
    while True:
        position  = input("Play {}, choose a position(row, col) 1 - 3.(example : 1,3 )'exit' for exit the game : ".format(player))
        if position == "exit":
            print("good bye !")
            break
        try:
            position1 = process_position(position)
        except:
            print("Error, position {} is not valid. ".format(position))
            continue
        if correct_position(position1):
            update_board(position1, player)
            show_board()
            if win(player):
                print("Player {} won!! ".format(player))
                break
            player = change_turn()
        else:
            print("Position {} is not valid ".format(position))
main()