class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        cols = len(grid[0])
        rows = len(grid)
        directions = [[-1,0],[0,-1],[0,1],[1,0]]
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j,0))
        
        while q:
            r, c, dist = q.popleft()
            for dr, dc in directions:
                nr = dr+r
                nc = dc+c
                if (nr>=0 and nc>=0 and nr<rows and nc<cols and grid[nr][nc]==2147483647):
                    grid[nr][nc] = dist+1
                    q.append((nr, nc, dist+1))
                




        