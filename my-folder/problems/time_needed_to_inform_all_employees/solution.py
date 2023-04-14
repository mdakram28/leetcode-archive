class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        child = [[] for _ in range(n)]
        max_time = 0

        for c, p in enumerate(manager):
            if p!=-1:
                child[p].append(c)

        def dfs(node, prev):
            nonlocal max_time
            # print(node,prev)
            max_time = max(max_time, prev)
            prev += informTime[node]
            for c in child[node]:
                dfs(c, prev)

        dfs(headID, 0)
        return max_time