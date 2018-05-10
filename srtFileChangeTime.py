#! python3
#coding=utf-8

import re

Zimu = r'''
    1
    00:00:00,450 --> 00:00:02,750
    《西部世界》第一季前情提要

    2
    00:00:01,260 --> 00:00:02,930
    欢迎来到西部世界
    Welcome to Westworld.

    3
    00:00:02,930 --> 00:00:04,580
    喜欢哪一个
    Which would you prefer?

    4
    00:00:05,390 --> 00:00:07,440
    这里就是答案
    This place is the answer

    5
    00:00:07,440 --> 00:00:09,730
    你一直自问的那个问题的答案
    to that question that you've been asking yourself.

'''
#srt文件查找时间方法
ZimuRegex = re.compile(r'\d\d\:\d\d\:\d\d,\d{2,3} --> \d\d\:\d\d\:\d\d,\d{2,3}')

ZimuFindall = ZimuRegex.findall(Zimu)

#Reduce_time(),减少时间
def reduceTime(time):
    #被减数
    reduceSecond = 0
    reduceMilliSecond = 500

    hour = int(time[0:2])
    hour_2 = int(time[17:19])

    minutes = int(time[3:5])
    minutes_2 = int(time[20:22])

    second = int(time[6:8])
    second_2 = int(time[23:25])

    MilliSecond = int(time[9:12])
    MilliSecond_2 = int(time[26:29])

    #The first time reduce
    if (MilliSecond - reduceMilliSecond) < 0:
        MilliSecond = 1000 + MilliSecond - reduceMilliSecond
        second = second - reduceSecond - 1
        if second < 0:
            second = 59 - reduceSecond
            minutes -= 1
            if minutes < 0:
                minutes = 59
                hour -= 1
                if hour < 0:
                    hour = 0
                    minutes = 0
                    second = 0
                    MilliSecond = 0
    else:
        MilliSecond -= reduceMilliSecond
        second -= reduceSecond

    #The second time reduce
    if (MilliSecond_2 - reduceMilliSecond) < 0:
        MilliSecond_2 = 1000 + MilliSecond_2 - reduceMilliSecond
        second_2 = second_2 - reduceSecond - 1
        if second_2 < 0:
            second_2 = 59 - reduceSecond
            minutes_2 -= 1
            if minutes_2 < 0:
                minutes_2 = 59
                hour_2 -= 1
                if hour < 0:
                    hour = 0
                    minutes = 0
                    second = 0
                    MilliSecond = 0
    else:
        MilliSecond_2 -= reduceMilliSecond
        second_2 -= reduceSecond

    hour = str(hour)
    hour_2 = str(hour_2)

    minutes = str(minutes)
    minutes_2 = str(minutes_2)

    second = str(second)
    second_2 = str(second_2)

    MilliSecond = str(MilliSecond)
    MilliSecond_2 = str(MilliSecond_2)

    #如果值长度为1，前面补0
    #time
    if len(hour) < 2:
        hour = '0' + hour

    if len(minutes) < 2:
        minutes = '0' + minutes

    if len(second) < 2:
        second = '0' + second

    if len(MilliSecond) < 2:
        MilliSecond = '00' + MilliSecond
    elif len(MilliSecond) < 3:
        MilliSecond = '0' + MilliSecond
    #time_2
    if len(hour_2) < 2:
        hour_2 = '0' + hour_2

    if len(minutes_2) < 2:
        minutes_2 = '0' + minutes_2

    if len(second_2) < 2:
        second_2 = '0' + second_2

    if len(MilliSecond_2) < 2:
        MilliSecond_2 = '00' + MilliSecond_2
    elif len(MilliSecond_2) < 3:
        MilliSecond_2 = '0' + MilliSecond_2

    time = hour + ':' + minutes + ':'+ second + ',' + MilliSecond + ' --> ' + hour_2 +  ':' + minutes_2 + ':'+ second_2 + ',' + MilliSecond_2
    return time

#add_time(),增加时间
def addTime(time):
    #被加数
    addSecond = 0
    addMilliSecond = 500

    hour = int(time[0:2])
    hour_2 = int(time[17:19])

    minutes = int(time[3:5])
    minutes_2 = int(time[20:22])

    second = int(time[6:8])
    second_2 = int(time[23:25])

    MilliSecond = int(time[9:12])
    MilliSecond_2 = int(time[26:29])
    
    #The first time add
    if (MilliSecond + addMilliSecond) > 999:
        MilliSecond = int(str(MilliSecond + addMilliSecond)[1:])
        second = second + addSecond + 1
        if second > 59:
            second = int(str(second)[1:])
            minutes += 1
            if minutes > 59:
                minutes = int(str(minutes)[1:])
                hour += 1
    else:
        MilliSecond += addMilliSecond
        second += addSecond
    #The second time add
    if (MilliSecond_2 + addMilliSecond) > 999:
        MilliSecond_2 = int(str(MilliSecond_2 + addMilliSecond)[1:])
        second_2 = second_2 + addSecond + 1
        if second_2 > 59:
            second_2 = int(str(second_2)[1:])
            minutes_2 += 1
            if minutes_2 > 59:
                minutes_2 = int(str(minutes_2)[1:])
                hour_2 += 1
    else:
        MilliSecond_2 += addMilliSecond
        second_2 += addSecond
    

    hour = str(hour)
    hour_2 = str(hour_2)

    minutes = str(minutes)
    minutes_2 = str(minutes_2)

    second = str(second)
    second_2 = str(second_2)

    MilliSecond = str(MilliSecond)
    MilliSecond_2 = str(MilliSecond_2)

    #如果值长度为1，前面补0
    #time
    if len(hour) < 2:
        hour = '0' + hour

    if len(minutes) < 2:
        minutes = '0' + minutes

    if len(second) < 2:
        second = '0' + second

    if len(MilliSecond) < 2:
        MilliSecond = '00' + MilliSecond
    elif len(MilliSecond) < 3:
        MilliSecond = '0' + MilliSecond
    #time_2
    if len(hour_2) < 2:
        hour_2 = '0' + hour_2

    if len(minutes_2) < 2:
        minutes_2 = '0' + minutes_2

    if len(second_2) < 2:
        second_2 = '0' + second_2

    if len(MilliSecond_2) < 2:
        MilliSecond_2 = '00' + MilliSecond_2
    elif len(MilliSecond_2) < 3:
        MilliSecond_2 = '0' + MilliSecond_2 

    time = hour + ':' + minutes + ':'+ second + ',' + MilliSecond + ' --> ' + hour_2 +  ':' + minutes_2 + ':'+ second_2 + ',' + MilliSecond_2
    return time

#define a timeChange list.(定义一个修改后时间的列表)
timeChange = []
for i in range(len(ZimuFindall)):
   timeChange += [ZimuRegex.sub(reduceTime(ZimuFindall[i]), ZimuFindall[i])]

#显示对比查看
#print(ZimuFindall)
#print(timeChange)

#利用split方法切割为列表
Zimu_list = Zimu.split('\n\n')
Zimu_list_2 = []
for i in range(len(Zimu_list)):
    Zimu_list_2 += [Zimu_list[i].split('\n    ')]

#find all time index start, and change the time.（找出所有时间下标起始位置,替换时间的值）
for m in range(len(ZimuFindall)):
    if ZimuFindall[m] in Zimu_list_2[m]:
        index = Zimu_list_2[m].index(ZimuFindall[m])
        Zimu_list_2[m].remove(ZimuFindall[m])
        Zimu_list_2[m].insert(index,timeChange[m])

#利用join方法将列表重组为字符串
new_ZimuList = []
for i in range(len(Zimu_list_2)):
    new_ZimuList += ['\n    '.join(Zimu_list_2[i])]

new_ZimuList_2 = '\n\n'.join(new_ZimuList)

print(new_ZimuList_2)

#输入字符串文本至E:\hello.txt文件夹中
#File = open('e:\hello.txt','w')
#File.write(new_ZimuList_2)
#File.close()