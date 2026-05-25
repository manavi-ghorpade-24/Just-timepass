class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #start from pacific ocean cells - do dfs - see how many cells can reach pacific 
        #start from atlantic - do dfs and find how many cells can reach atlantic
        #coz we are strting from ocean to cell = height equal or greater 
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        res = []

        directions =[[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(r,c, visitset, prevheight):
            if (r,c) in visitset or r<0 or c<0 or r>=rows or c>=cols or heights[r][c]<prevheight:
                return
            visitset.add((r,c))
            for nr,nc in directions:
                dfs(r+nr,c+nc, visitset, heights[r][c])

        for r in range(rows): #1st and last col
            dfs(r,0, pac, heights[r][0])
            dfs(r,cols-1, atl, heights[r][cols-1])

        for c in range(cols): #1st and last row
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        
        #comman in sets 
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res 



