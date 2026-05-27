class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        indegree = [0]*numCourses
        adj = defaultdict(list)
        q = deque()

        for v , u in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        
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
            return res
        
        return []
