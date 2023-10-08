class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def dfs(x, y):
            if x < 0 or y < 0 or x > row-1 or y > col-1:
                return False
            if grid[x][y] == "1":
                grid[x][y] = "0"
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)
                return True
            return False
        
        cnt = 0
        for r in range(row):
            for c in range(col):
                if dfs(r, c) == True:
                    cnt += 1
        return cnt
