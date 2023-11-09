class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        count = 0
        def dfs(at, p):
            nonlocal count
            total = values[at]
            for to in g[at]:
                if to != p:
                    total += dfs(to, at)
            if total % k == 0:
                count += 1
            return total
        
        dfs(0, None)
        return count