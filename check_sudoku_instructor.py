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
               
def check_sudoku(p):
    n=len(p)
    digit=1
    while digit<=n:
        i=0
        while i<n:
            row_count=0
            col_count=0
            j=0
            while j<n:
                if p[i][j]==digit:
                    row_count=row_count+1
                if p[j][i]==digit:
                    col_count=col_count+1
                j=j+1
            if row_count!=1 or col_count!=1:
                return False
            i=i+1
        digit=digit+1
    return True

print (check_sudoku(correct))
print (check_sudoku(incorrect))
print (check_sudoku(incorrect2))
print (check_sudoku(incorrect3))
print (check_sudoku(incorrect4))
print (check_sudoku(incorrect5))
