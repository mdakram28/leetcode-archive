class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        visited = [False] * n
        edges = [[] for i in range(n)]

        for i1, i2 in connections:
            edges[i1].append(i2)
            edges[i2].append(i1)

        def set_conn_comp(i):
            if visited[i]:
                return
            visited[i] = True
            # num_nodes = 1
            for to in edges[i]:
                set_conn_comp(to)
            return
        
        num_comp = 0
        # total_cables = 0
        for i in range(n):
            if not visited[i]:
                set_conn_comp(i)
                num_comp += 1

        req_cables_disconn = n - num_comp
        free_cables = len(connections) - req_cables_disconn
        if free_cables < (num_comp-1):
            return -1
        else:
            return (num_comp-1)