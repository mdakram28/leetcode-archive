class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = collections.defaultdict(dict)
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            edges[a][b] = val
            edges[b][a] = 1/val
        
        visited = {}
        @cache
        def dfs(node, target, parent):
            if node in visited:
                return None
            if node == target and edges[node]:
                return 1.0
            visited[node] = True
            for to, mul in edges[node].items():
                if to == parent:
                    continue
                val = dfs(to, target, node)
                if val:
                    return val * mul
            return None

        ret = []
        for start, end in queries:
            visited.clear()
            val = dfs(start, end, None)
            if val:
                ret.append(val)
            else:
                ret.append(-1.0)
        
        return ret