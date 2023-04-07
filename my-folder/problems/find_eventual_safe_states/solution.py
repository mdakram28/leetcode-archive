class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        is_safe = [None] * n

        # for node in range(n):
        #     for to in graph[node]:
        #         parents[to].append(node)

        def mark_safe(node):
            if is_safe[node] is not None:
                return is_safe[node]

            is_safe[node] = False
            safe = True
            for to in graph[node]:
                if not mark_safe(to):
                    safe = False
            is_safe[node] = safe
            return safe
        
        return [node for node in range(n) if mark_safe(node)]