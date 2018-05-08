#！python3
# This is a PrintStr program

spam = ['apples', 'bananas', 'tofu', 'cats']
spam_0 = []
spam_1 = ['apples']
spam_2 = ['apples', 'bananas']
spam_3 = ['apples', 'bananas', 'tofu']

def returnStr(_list):
    _str = ''
    length = len(_list)
    if length == 0:
        return ''
    elif length == 1:
        return _list[0]
    elif length == 2:
        return _list[0]+' and '+_list[1]
    else:
        for i in range(0,len(_list)-2):
            _str += str(_list[i]) + ', '
        return _str + _list[-2] + ' and ' + _list[-1] 

print(returnStr(spam))
print(returnStr(spam_0))
print(returnStr(spam_1))
print(returnStr(spam_2))
print(returnStr(spam_3))