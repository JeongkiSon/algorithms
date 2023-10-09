class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Using DFS
        '''
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(x, y):
            if x < 0 or y < 0 or x > rows-1 or y > cols-1:
                return 0
            if grid[x][y] == 1:
                grid[x][y] = -1
                return 1 + dfs(x-1, y) + dfs(x+1, y) + dfs(x, y-1) + dfs(x, y+1)
            return 0

        islands = []
        for r in range(rows):
            for c in range(cols):
                islands.append(dfs(r, c))
            
        return max(islands)
        '''

        # Using BFS
        from collections import deque

        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(x, y):
            area = 1
            q = deque()
            q.append((x, y))
            visited.add((x, y))
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == 1 and
                        (nr, nc) not in visited):
                        area += 1
                        visited.add((nr, nc))
                        q.append((nr, nc))
            return area
        
        islands = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    islands.append(bfs(row, col))

        if islands:
            return max(islands)
        else:
            return 0
