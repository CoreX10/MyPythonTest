#learn regex.

'''
#非正则表达式版本   
def isPhoneNumber(text):
    #是否为长度为12
    if len(text) != 12:
        return False
    #前三项是否为数字
    for i in range(0,3):
        if not text[i].isdecimal:
            return False
    #第四项是否为“-”
    if text[3] != '-':
        return False
    #第五项到第七项是否为数字
    for i in range(4,7):
        if not text[i].isdecimal:
            return False
    #第八项是否为“-”        
    if text[7] != '-':
        return False
    #第九项到第十二项是否为数字
    for i in range(8,12):
        if not text[i].isdecimal:
            return False
    #若满足以上所有条件，返回True
    return True

print('415-555-4242 is a Phone Number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a Phone Number:')
print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone Number found: ' + chunk)
print('done') 
'''
#正则表达式版本↓（re模块）
import re
#向re.compile()传入一个字符串值，表示正则表达式，返回一个Regex模式对象。(\d表示单个数字，\d{3} == \d\d\d)
PhoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
#可以利用括号进行分组，（）
PhoneNumberRegex2 = re.compile(r'(\d{3})-(\d{3}-\d{4})')
'''
search()方法:
使用search()方法查找第一次所匹配的字符。没找到返回None;如果找到，返回一个Match对象，Match对象有一个group()方法，
返回字符串中实际匹配的文本。
'''
mo = PhoneNumberRegex.search(' My Number is 415-555-4242, 455-554-4845 is my office number.')
#未分组↑
#  分组↓
mo2 = PhoneNumberRegex2.search(' My Number is 415-555-4242, 455-554-4845 is my office number.')
'''
findall()方法:
使用findall()方法查找所有匹配的字符，返回一组字符串的列表。
'''
mo_findall = PhoneNumberRegex.findall('My Number is 415-555-4242, 455-554-4845 is my office number.')
#未分组↑
#  分组↓
mo2_findall = PhoneNumberRegex2.findall('My Number is 415-555-4242, 455-554-4845 is my office number.')

#search()
print('1、MO:')
print(mo)
print('Phone Number found: ' + mo.group())

#findall()
print('\n2、MO_findall:')
print(mo_findall)
print('MO_findall[0]:\n' + mo_findall[0])

#分组后,search()方法
print('\n3、MO2:')
print(mo2,end='')
print(', ' + 'type:' + str(type(mo2)))
print('Phone Number found: ' + mo2.group())
print('MO2.group(0):' + mo2.group(0))
print('MO2.group(1):' + mo2.group(1))
print('MO2.group(2):' + mo2.group(2))
#一次取得所有分组，使用 groups() 方法,返回一个字符串的元祖
print('Mo2.groups():',end = '')
print( mo2.groups())

#分组后，findall()方法
print('\n4、MO2_findall:')
print(mo2_findall,end = '')
print(', ' + 'type:' + str(type(mo2_findall)))
print(mo2_findall[0][1])