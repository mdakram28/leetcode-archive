class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        ret = []
        prev = []
        def dfs(node):
            if node == target:
                ret.append([*prev, node])
            else:
                prev.append(node)
                for to in graph[node]:
                    dfs(to)
                prev.pop()
        dfs(0)
        return ret
                