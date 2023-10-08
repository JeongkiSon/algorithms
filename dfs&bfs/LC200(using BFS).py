class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
      
        row = len(grid)
        col = len(grid[0])
        visited = set()

        def bfs(x, y):
            q = deque()
            q.append((x,y))
            visited.add((x, y))
            while q:
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr <= row-1 and 0 <= nc <= col-1
                    and grid[nr][nc] == "1"
                    and (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
        
        cnt = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    cnt += 1
                    print(r,c)
        return cn

  '''
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
    '''
