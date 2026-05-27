class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        res =[]
        adj = defaultdict(list)
        indegree = [0]*numCourses
        q = deque()

        for u, v in prerequisites:
            adj[v].append(u) 
            indegree[u]+=1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            n = q.popleft()
            res.append(n)
            for nei in adj[n]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if len(res) == numCourses:
            return True

        return False
        

    
       
        

        