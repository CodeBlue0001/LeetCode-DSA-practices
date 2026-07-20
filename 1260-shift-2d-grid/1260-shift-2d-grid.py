class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def fn(mat):
            l = len(mat)
            n = len(mat[0])
            lst = [i for row in mat for i in row]
            lst = [lst[-1]] + lst[:-1]
            temp = []
            for r in range(0, len(lst), n):
                temp += [lst[r:r+n]]
            return temp
            
        for i in range(k):
            grid=fn(grid)
                    
        return grid