board = {1: ' ', 2: ' ', 3: ' ', 
         4: ' ', 5: ' ', 6: ' ', 
         7: ' ', 8: ' ', 9: ' '}


def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')

    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')


printBoard(board)



def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False

    return True



def checkWin():
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True

    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True

    elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True

    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True

    elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True

    elif board[3] == board[5] and board[3] == board[7] and board[3] != ' ':
        return True

    elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True

    elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True

    else:
        return False


def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True

    elif board[1] == board[4] and board[1] == board[7] and board[1] == mark:
        return True

    elif board[1] == board[5] and board[1] == board[9] and board[1] == mark:
        return True

    elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
        return True

    elif board[3] == board[6] and board[3] == board[9] and board[3] == mark:
        return True

    elif board[3] == board[5] and board[3] == board[7] and board[3] == mark:
        return True

    elif board[4] == board[5] and board[4] == board[6] and board[4] == mark:
        return True

    elif board[7] == board[8] and board[7] == board[9] and board[7] == mark:
        return True

    else:
        return False


def spaceIsFree(position):
    if(board[position] == ' '):
        return True

    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)

        if checkDraw():
            print("Draw!")
            exit()

        elif checkWin():
            if letter == 'X':
                print("Bot wins!")
                exit()

            else:
                print("Player wins!")
                exit()

    else:
        print('Could insert there!')
        position = int(input("Enter new Position: "))
        insertLetter(letter, position)


def player_move():
    position = int(input("Enter Position: "))
    insertLetter(letter='0', position=position)

bot = 'X'

def bot_move():
    best_score = -800
    best_move = 0

    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > best_score):
                best_score = score
                best_move = key

    insertLetter(bot, best_move)


def minimax(board, depth, isMaximizing):
    if checkWhichMarkWon(bot):
        return 1

    elif checkWhichMarkWon('0'):
        return -1

    elif checkDraw():
        return 0

    if isMaximizing:
        best_score = -800

        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > best_score):
                    best_score = score

        return best_score

    else:
        best_score = 800

        for key in board.keys():
            if board[key] == ' ':
                board[key] = '0'
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < best_score):
                    best_score = score

        return best_score



while True:
    bot_move()
    if checkDraw():
        break

    elif checkWin():
        break
    
    player_move()
    
    if checkDraw():
        break

    elif checkWin():
        break
