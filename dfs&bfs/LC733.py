class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pixel = image[sr][sc]
        if pixel == color: return image

        row = len(image)
        col = len(image[0])

        def dfs(x, y):
            if x<0 or y<0 or x>row-1 or y>col-1:
                return -1
            if image[x][y] == pixel:
                image[x][y] = color
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)
                return 0
            return -1

        dfs(sr, sc)
        return image
