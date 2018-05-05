# This is a TicTacToe Game program

import time

R = True

while R == True:

    theBoard = {
        'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ',
        'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
        'low-L' : ' ', 'low-M' : ' ', 'low-R' : ' '
    }

    #define a tip for initial Range
    def initialRange():
        print('top-L | top-M | top-R')
        print('------+-------+------')
        print('mid-L | mid-M | mid-R')
        print('------+-------+------')
        print('low-L | low-M | low-R')

    #victorious situation
    VictoriousStiuation = [
        ['top-L','top-M','top-R'],['top-L','mid-M','low-R'],['top-L','mid-L','low-L'],['top-M','mid-M','low-M'],
        ['top-R','mid-R','low-R'],['top-R','mid-M','low-L'],['mid-L','mid-M','mid-R'],['low-L','low-M','low-R']
    ]

    #Define an array to store the input coordinates, Avoid repeated input
    AlreadyInputted = []

    def printBoard(board):
        print(board['top-L'] + '|' + board['top-M'] + '|'+ board['top-R'])
        print('-+-+-')
        print(board['mid-L'] + '|' + board['mid-M'] + '|'+ board['mid-R'])    
        print('-+-+-')
        print(board['low-L'] + '|' + board['low-M'] + '|'+ board['low-R'])

    #Initialization turn is X
    turn = 'X'
    #Initialization win is 0. 
    # In the loop, if win equals 1, break the loop;
    #              if win equals 0, continue the loop.
    # After the loop, if win equals 1, Prompt the winning party; 
    #                 if win equals 0, prompt It ends in a draw. 
    win = 0

    for i in range(9):

        if win == 1:
            break

        printBoard(theBoard)
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        #Whether the input is correct or not(输入是否正确)
        while move not in theBoard.keys():
            print('type error, please try again, The input range is: ')
            initialRange()
            move = input()
        #Whether the input is repeated or not(输入是否重复)
        while move in AlreadyInputted:
            print('Already Inputted! try other word.')
            move = input()

        #The input coordinates are assigned to AlreadyInputted(已输入坐标赋值给AlreadyInputted)
        AlreadyInputted += [move]
        #X moving coordinates（X移动的坐标）
        print('The X moving coordinates: ' + str(AlreadyInputted[::2]))
        #O moving coordinates
        print('The o moving coordinates: ' + str(AlreadyInputted[1::2]))

        #Judge whether X wins.The fifth step begins(i==4).
        if i > 3 & i % 2 == 0:
            X_AlreadyInputted = set(AlreadyInputted[::2])
            #Using the set () method to perform the parallel operation(运用set（）方法进行并集操作)
            #X moving coordinates | Each of the winning list(X已输入移动坐标列表 | 获胜情形列表的每一项)
            for y in range(len(VictoriousStiuation)):
                VS = set(VictoriousStiuation[y])
                #After the integration, The result is the same as X_AlreadyInputted, The X Win!
                #(交集之后，结果和X_已输入列表一样，则X获胜)
                if (X_AlreadyInputted | VS) == X_AlreadyInputted:
                    print('The X Win!')
                    win = 1

        #Judge whether O wins.The sixth step begins(i==5).
        if i > 3 & i % 2 == 1:        
            O_AlreadyInputted = set(AlreadyInputted[1::2])
            #O moving coordinates | Each of the winning list(O已输入移动坐标列表 | 获胜情形列表的每一项)
            for y in range(len(VictoriousStiuation)):
                VS = set(VictoriousStiuation[y])
                #After the integration, The result is the same as O_AlreadyInputted, The O Win!
                #(交集之后，结果和O_已输入列表一样，则O获胜)
                if (O_AlreadyInputted | VS) == O_AlreadyInputted:
                    print('The O Win!')
                    win = 1 

        #X,O交替输入
        theBoard[move] = turn 
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    #Flat situation
    if win == 0:
        print('It ends in a draw!')
    printBoard(theBoard)

    #type 'y' or 'yes' or 'YES' or 'Yes' to restart the game.
    print('  Do you want to start another game again?')
    print('  if you want, Please type "y" to start another game, or type anything to end ')
    Values = input()
    if Values == 'y':
        R = True
    else:
        R = False
        print(' Out of 3 seconds...')
        for i in range(3,0,-1):
            time.sleep(1)
            print(' ' + i)
        time.sleep(1)
        print(' End.')

    