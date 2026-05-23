class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        ans = 0
        directions = [[-1,0],[0,-1],[1,0],[0,1]]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j,0))
        
        while q:
            r, c, t = q.popleft()
        
            for dr, dc in directions:
                nr = dr+r
                nc = dc+c
                if nr>=0 and nc>=0 and nr<rows and nc<cols and grid[nr][nc]==1:
                    grid[nr][nc] = 2
                    fresh -= 1 
                    q.append((nr, nc, t+1))
      
            ans = t
            

  
        if fresh == 0:
            return ans

        else:
            return -1 
        


