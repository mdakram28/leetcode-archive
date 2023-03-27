class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = [False] * len(edges)
        depth = [-1] * len(edges)
        num_nodes = len(edges)

        # for f, t in enumerate(edges):
        #     is_start[t] = False
        
        def visit(n):
            while n != -1 and not visited[n]:
                visited[n] = True
                n = edges[n]

        def get_cycle(n):
            orig = n
            d = 0
            while n != -1:
                if visited[n]:
                    return -1
                if depth[n] >= 0:
                    # visit(orig)
                    return d - depth[n]
                depth[n] = d
                # visited[n] = True
                n = edges[n]
                d += 1
            # visit(orig)
            return -1
        
        max_d = -1
        for n in range(num_nodes):
            # if is_start[n]:
            max_d = max(max_d, get_cycle(n))
            visit(n)

        return max_d