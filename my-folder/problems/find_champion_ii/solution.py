class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        parents = [[] for _ in range(n)]
        for n1, n2 in edges:
            parents[n2].append(n1)
        
        visited = [False] * n
        
        root = None
        
        def visit(at):
            nonlocal root
            visited[at] = True
            if len(parents[at]) == 0:
                if root is None:
                    root = at
                    return True
                else:
                    return False
            else:
                for to in parents[at]:
                    if not visited[to]:
                        if not visit(to):
                            return False
            return True
        
        for node in range(n):
            if not visited[node]:
                if not visit(node):
                    return -1
        
        return root