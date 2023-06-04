class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        ans = 0
        for start in range(n):
            if visited[start]: continue
            q = [start]
            ans += 1
            for at in q:
                for to in range(n):
                    if (not isConnected[at][to]) or visited[to]: continue
                    visited[to] = True
                    q.append(to)

            
        
        return ans