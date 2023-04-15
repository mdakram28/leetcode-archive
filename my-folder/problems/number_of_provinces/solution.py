class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def travel(at):
            visited[at] = True
            for to in range(n):
                if isConnected[at][to] and not visited[to]:
                    travel(to)
        
        ans = 0
        for at in range(n):
            if not visited[at]:
                travel(at)
                ans += 1
        
        return ans