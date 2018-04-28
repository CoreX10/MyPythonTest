#This is a guess number game.
import random

_number = random.randint(1,20) #生成随机数

def guess():
    #捕获异常,判断输入值得类型是否正确
    try:
        type_number = int(input()) #输入一个数
    except ValueError:
        print('Value Error, Please try again.')
        guess()
    else:       
        for i in range(1,7):  #设置猜测次数最多为6次
            #进行判断输入是否合理
            if type_number <= 20 and type_number >=1:
                if type_number > _number:
                    print('You guess is too big!')
                    type_number = int(input())
                if type_number < _number:
                    print('You guess is too small!')
                    type_number = int(input())               
                else:
                    break
            else:
                print('Wrong Number, Please try again. The number between 1 and 20!!!')
                type_number = int(input())
        #判断猜测在给定次数内是否正确
        if type_number == _number:
            print('You Win! The number is '+ str(_number))
        else:
            print('Sorry, You lose. The number is '+ str(_number)) 


print(' I am thinking of a number between 1 and 20. \n Take a guess!')

guess()





