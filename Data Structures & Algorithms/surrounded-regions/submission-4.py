class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #so basically start from edge 0's ,
        #  do dfs, visit other nei 0's, mark visited
        # in the end check which 0's are not visited and covert to X
        
        rows = len(board)
        cols = len(board[0])
        visited = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(r, c, visited):
            if r<0 or c<0 or r>= rows or c>=cols or (r,c) in visited or board[r][c] == "X":
                return
            visited.add((r,c))
            for nr, nc in directions:
                dfs(nr+r, nc+c, visited)
        
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0, visited)
            if board [r][cols-1] == "O":
                dfs(r, cols-1, visited)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c, visited)
            if board[rows-1][c] == "O":
                dfs(rows-1, c, visited)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"


            
        