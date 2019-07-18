correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

def check_sudoku(x):
   
    for h in x:
        for i in h:
            if i == str(i):
                return False   
            if i !=int(i):
                return False

    k=0
    while True:
        if k<len(x[0]):
            j=1
            while j<=len(x[0]):
                if j in x[k]:
                    j=j+1
                else:
                    return False
            k=k+1
            
        else:
            if j>len(x[0]):
                break
            else:
                False
    
    k=0
    s=0
    
    while s<len(x[0]):
        t=0
        L=[]
        while s<len(x[0]):
            if t<len(x[0]):
                L.append(x[t][s])
                t=t+1
            else:
                break
        
        while True:
            if s<len(x[0]):
                u=1
                while s<len(x[0]):
                    if u in L:
                        u=u+1
                    else:
                        if u>len(x[0]):
                            break
                        else:
                            return False
            s=s+1
            break
    return True
            
print (check_sudoku(correct))
print (check_sudoku(incorrect))
print (check_sudoku(incorrect2))
print (check_sudoku(incorrect3))
print (check_sudoku(incorrect4))
print (check_sudoku(incorrect5))
