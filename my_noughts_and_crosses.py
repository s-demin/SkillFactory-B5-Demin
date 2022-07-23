print('''Нумерация ячеек игрового поля начинается с 0,
           как показано на схеме:''')
print()
print(" 0 | 1 | 2 ")
print("-----------")
print(" 3 | 4 | 5 ")
# print(board[4], end=" | ")
# print(board[5])
print("-----------")
print(" 6 | 7 | 8 ")
print()
# print()
print("Начинаем игру:")
print()
# print()



# Игровое поле
board = ["  ", " ", " ",
         "  ", " ", " ",
         "  "," ", " "]

# Выигрышные комбинации
winning = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

# Рисуем игровое поле
def show_board():
    print(board[0], end=" | ")
    print(board[1], end=" | ")
    print(board[2])
    print("-----------")
    print(board[3], end=" | ")
    print(board[4], end=" | ")
    print(board[5])
    print("-----------")
    print(board[6], end=" | ")
    print(board[7], end=" | ")
    print(board[8])
    print()

# Ход в ячейку
def move(step,symbol):
    board[step] = symbol

# Определение победителя
def get_result():
    winner = ""
 
    for i in winning:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            winner = "Крестик"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            winner = "Нолик"   
             
    return winner

# Игра 
game_over = False
player_x = True
 
while not game_over:
 
    show_board()
 
    # Запрос ячейки
    if player_x:
        symbol = "X"
        step = int(input("Ходит Крестик: "))
    else:
        symbol = "O"
        step = int(input("Ходит Нолик: "))
 
    move(step,symbol) # делаем ход в указанную ячейку
    winner = get_result() # определим победителя
    if winner != "":
        game_over = True
    else:
        game_over = False
 
    player_x = not(player_x)        
 
# Конец игры        
show_board()
print("Выиграл", winner) 