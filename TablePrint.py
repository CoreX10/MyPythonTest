#This is a Table_Print program

#define table data.
tableData = [
    ['apples','oranges','cherries','banana'],
    ['Alice','Bob','Carol','David'],
    ['dogs','cats','moose','goose']    
]

def printTable(tableData):
    #colwidths用来存放输出列的最大长度
    colWidths = []

    for i in range(len(tableData)):
        m = 0
        #比较大小，较大值赋值给m
        for j in range(len(tableData[i])):
            if m >= len(tableData[i][j]):
                m = m
            else:
                m = len(tableData[i][j])
        #把m添加到clowidths列表中
        colWidths += [m]
    #输出整理后列表
    for i in range(4):
        for j in range(3):
            #print(,end=' ')方法，换行改为空格
            print(tableData[j][i].rjust(colWidths[j])+' ',end=' ')
        print('')
#提示信息
print('The List content is:\n')
printTable(tableData)