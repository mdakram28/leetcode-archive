class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def get_repr(node):
            while node != parent[node]:
                node = parent[node]
            return node
        
        def merge_repr(r1, r2):
            parent[r1] = r2
        
        def compact(node):
            if node == parent[node]:
                return node
            else:
                parent[node] = compact(parent[node])
                return parent[node]

        for n1, n2 in edges:
            r1 = get_repr(n1)
            r2 = get_repr(n2)
            merge_repr(r1, r2)
            compact(n1)
            compact(n2)
        
        for node in range(n):
            compact(node)

        counts = {}
        for p in parent:
            counts[p] = counts.get(p, 0) + 1
        ret = 0
        total_nodes = 0
        for c in counts.values():
            ret += total_nodes * c
            total_nodes +=c 


        return ret
