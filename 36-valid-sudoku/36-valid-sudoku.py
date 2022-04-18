class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(board)
        
        check_row_array = [0 for _ in range(10)]
        check_col_array = [0 for _ in range(10)]
        check_3X3_array = [0 for _ in range(10)]
        
        for i in range(9):
        
            for j in range(9):
                #row check
                if board[i][j] != '.':
                    if check_row_array[int(board[i][j])] == 1:
                        print("row")
                        print(i, j)
                        print(check_row_array)
                        return False
                    else:
                        check_row_array[int(board[i][j])] += 1
                        
                #col check
                if board[j][i] != '.':
                    if check_col_array[int(board[j][i])] == 1:
                        print("col")
                        print(j, i)
                        print(check_col_array)
                        return False
                    else:
                        check_col_array[int(board[j][i])] += 1
            
            #clear [0*10]
            for j in range(10):
                check_row_array[j] = 0
                check_col_array[j] = 0
        
        #3X3 check
        for x in range(0,9,3):
            for y in range(0,9,3):
                for i in range(3):
                    for j in range(3):
                        if board[x+i][y+j] != '.':
                            if check_3X3_array[int(board[x+i][y+j])] == 1:
                                print("3X3")
                                print(x+i, y+j)
                                print(check_3X3_array)
                                return False
                            else:
                                check_3X3_array[int(board[x+i][y+j])] += 1
                
                #clear [0*10]
                for i in range(10):
                     check_3X3_array[i] = 0
                           
        return True