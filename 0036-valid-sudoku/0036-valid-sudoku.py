class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row=len(board)
        column=len(board[0])

        for Row in board:
            print(Row)

        def is_row_valid(r):
            visited=[]
            for j in range(column):
                if board[r][j] !='.' and board[r][j] not in visited:
                    visited+=[board[r][j]]
                elif board[r][j] !='.' and board[r][j] in visited:
                    print(visited,board[r][j])
                    return False
            return True

        def is_column_valid(r):
            visited=[]
            for i in range(row):
                if board[i][r]!="." and board[i][r] not in visited:
                    visited+=[board[i][r]]
                elif board[i][r]!="." and board[i][r] in visited :
                    print(visited,board[i][r])
                    return False
            return True
        def sub_matrix_search():
            # m,n=3,3

            sm,m=0,3
            while m<=row :
                sn, n = 0, 3
                while n <= 9:  # checks column bands (0-3), (3-6), (6-9) for this row band
                    visited = []
                    for i in range(sm, m):
                        for j in range(sn, n):
                            val = board[i][j]
                            if val != ".":
                                if val in visited:
                                    return False
                                visited.append(val)
                    sn += 3
                    n += 3
                sm += 3
                m += 3

            return True

        # sub_matrix_search()
        if sub_matrix_search():           
            for i in range(row):
                if is_row_valid(i)==False or is_column_valid(i)==False:
                    #  here have to add the 3x3 1-9 rule to validate the the sudoku
                    return False
            return True
        return False
        