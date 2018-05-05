#This is a PrintGrid program

#defind a grid.
grid = [
    ['.','.','.','.','.','.'],
    ['.','0','0','.','.','.'],
    ['0','0','0','0','.','.'],
    ['0','0','0','0','0','.'],
    ['.','0','0','0','0','0'],
    ['0','0','0','0','0','.'],
    ['0','0','0','0','.','.'],
    ['.','0','0','.','.','.'],
    ['.','.','.','.','.','.']    
]

#Obtain x and y.
x = len(grid[0])
y = len(grid)

#先竖后横，竖_循环在横_循环内
for i in range(x):
    for j in range(y):
        #end = '', Not end with a change of line
        print (grid[j][i],end = '')
    #'\n'change line 
    print('\n')   