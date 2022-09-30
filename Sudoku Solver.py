import numpy as np

# grid = [[0,0,0, 0,0,0, 0,0,0],
#         [0,0,0, 0,0,0, 0,0,0],
#         [0,0,0, 0,0,0, 0,0,0],
#         [0,0,0, 0,0,0, 0,0,0],
#         [0,0,0, 0,0,0, 0,0,0],
#         [0,0,0, 0,0,0, 0,0,0],
#         [0,0,0, 0,0,0, 0,0,0],
#         [0,0,0, 0,0,0, 0,0,0],
#         [0,0,0, 0,0,0, 0,0,0]]

grid = [[3,4,0, 0,0,0, 0,0,2],
        [0,9,0, 0,0,0, 0,0,5],
        [1,0,5, 0,0,0, 0,0,4],

        [0,1,2, 0,0,9, 0,0,0],
        [6,8,0, 0,5,3, 0,4,1],
        [9,0,0, 0,0,0, 8,0,0],
        
        [2,0,0, 8,0,6, 0,0,0],
        [0,6,0, 0,0,4, 0,0,0],
        [0,0,0, 0,9,0, 3,0,0]]

def checker(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i]==n:
            return False
    for i in range(0,9):
        if grid[i][x]==n:
            return False
    xX = (x//3)*3
    yY = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[yY+i][xX+j]==n:
                return False
    return True
# print(checker(0,2,9))
def solver():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x]==0:
                for n in range(10):
                    if checker(y,x,n):
                        grid[y][x]=n
                        solver()
                        grid[y][x]=0
                return
    print(np.matrix(grid))


solver()
