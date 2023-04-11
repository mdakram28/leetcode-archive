class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n

        def check_node(at, c):
            if color[at]:
                return color[at] == c
            color[at] = c
            c = 3-c
            for to in graph[at]:
                if not check_node(to, c):
                    return False
            return True
        
        for i in range(n):
            if not color[i] and not check_node(i, 1):
                return False
        
        return True

            