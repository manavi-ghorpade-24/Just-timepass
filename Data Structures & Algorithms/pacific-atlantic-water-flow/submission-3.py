class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #start from pacific ocean cells - do dfs - see how many cells can reach pacific 
        #start from atlantic - do dfs and find how many cells can reach atlantic
        #coz we are strting from ocean to cell = height equal or greater 
        row = len(heights)
        col = len(heights[0])
        pac = set()
        atl = set()

        directions =[[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(r, c, visit, prevheight):
            if ((r,c) in visit or r<0 or c<0 or r>=row or c>=col or heights[r][c]<prevheight): #already visited
               return
            visit.add((r,c))
            for nr,nc in directions:
                dfs(r+nr, c+nc, visit, heights[r][c])

        #on first row , last row
        for c in range(col):
            dfs(0,c, pac, heights[0][c]) #need to pass height coz we are checking heights =>
            dfs(row-1,c,atl, heights[row-1][c]) #pass height as previous height

        for r in range(row):
            dfs(r,0,pac,heights[r][0])
            dfs(r,col-1,atl,heights[r][col-1])
        
        #now we have all positions that can reach pac and alt in set 
        #lets take the comman one
        res = []
        for r in range(row):
            for c in range(col):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res



