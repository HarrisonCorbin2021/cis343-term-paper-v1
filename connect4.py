#######################################################
#
# Harrison Corbin
#
#######################################################
import sys

class Connect4():

    num_Cols = 7
    num_Rows = 6
    board = [['x' for i in range(0, 7 , 1)] for j in range(0, 6, 1)]
        
    def print_board(board):
        for i in range (0, Connect4.num_Cols - 1, 1):
            #sys.stdout.write(str(i))
            print("\n")
            for j in range(0, Connect4.num_Rows + 1, 1):
                sys.stdout.write(str(board[i][j]))

    def verticalWin(board,player):
        count = 0
        # check for horizontal wins
        #print(board[2][2])
        for i in range(0, Connect4.num_Rows - 1, 1):
            for j in range(0, Connect4.num_Cols - 1, 1):
                    while board[i + count][j] == player:
                        count += 1
                        print(count)
                        #print("A")
                        if count >= 4:
                            #print("I worked")
                            return True
                        if i + count >= Connect4.num_Rows:
                            count = 0
                            #print(j + count)
                            #print ("B")
                            break

    def horizontalWin(board,player):
        count = 0
        # check for horizontal wins
        #print(board[2][2])
        for i in range(0, Connect4.num_Cols - 1, 1):
            for j in board[i]:
                    if j == player:
                        count += 1
                        print(count)
                        print(i)
                        #print("A")
                        if count >= 4:
                            #print("I worked")
                            return True
                    else:
                        count = 0

    def diagonalLWint(board,player):
        count = 0
        # check for diagonal right wins
        for i in range(0, Connect4.num_Rows - 3, 1):
            for j in range(0, Connect4.num_Cols - 3, 1):
                    while board[i + count][j + count] == player:
                        count += 1
                        if count >= 4:
                            return True
                        if i + count >= Connect4.num_Cols - 1:
                            break
                        if j + count >= Connect4.num_Rows:
                            break
                    

    def diagonalRWin(board,player):     
        count = 0
        # check for diagonal left wins
        for i in range(0, Connect4.num_Rows - 3, 1):
            for j in range(0, Connect4.num_Cols - 3, 1):
                    while board[i + count][j - count] == player:
                        count += 1
                        print(count)
                        if i + count >= Connect4.num_Rows or j - count < 0:
                            break
                    if count >= 4:
                        return True
                    
    def winCheck(board, player):
        #print ("F")
        return Connect4.horizontalWin(board,player) or Connect4.verticalWin(board,player) or Connect4.diagonalRWin(board,player) #or Connect4.diagonalLWin(board,player)

    def PlayerTurn(board, player):
        Connect4.print_board(board)
        print("\n")
        inp = input()
        inp = ord(inp[0]) - ord("a")
        #Check for a valid input
        #print(inp)
        while inp > 7 or inp < 0:
            if inp == 16:
                print("Goodbye.")
                quit()
            print("Not a valid entry.")
            inp = input()
            inp = ord(inp[0]) - ord("a")
        #if top row is empty
        if board[0][inp] == 'x':
            for i in range(Connect4.num_Cols - 2, 0, -1):
                if board[i][inp] == 'x':
                    board[i][inp] = player
                    break
        else:
            print("That column is full. Please choose another")
        if Connect4.winCheck(board, player):
            if player == 1:
                print ('Congratulations, Player 1. You Win.')
            else:
                print ('Congratulations, Player 2. You Win.')
            quit()
        if player == 1:
            Connect4.PlayerTurn(board, 2)
        else:
            Connect4.PlayerTurn(board, 1)

if __name__ == '__main__':
    board = Connect4.board
    #board.print_board()
    Connect4.PlayerTurn(board,1)