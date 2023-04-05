class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        visiting = [None] * n
        parent = [None] * n
        g = [set() for i in range(n)]

        for n1, n2 in edges:
            g[n1-1].add(n2-1)
            g[n2-1].add(n1-1)

        common_nodes = None
        
        def visit(at, p):
            nonlocal common_nodes
            if visiting[at] is not None:
                common_nodes = (at, p)
                return True
            visiting[at] = True

            parent[at] = p
            for to in g[at]:
                if to == p:
                    continue
                if visit(to, at):
                    return True

            visiting[at] = False
            return False

        critical_edges = set()
        visit(0, None)
        # print(common_nodes)
        at = common_nodes[0]
        while not visiting[at]:
            p = parent[at]
            critical_edges.add((min(at, p), max(at, p)))
            at = p

        # print(at)
        at2 = common_nodes[1]
        while at2 != at:
            p = parent[at2]
            critical_edges.add((min(at2, p), max(at2, p)))
            at2 = p

        critical_edges.add((min(common_nodes), max(common_nodes)))
        

        
        # print(common_nodes, visiting, critical_edges)

        for n1, n2 in edges[::-1]:
            edge = (min(n1-1, n2-1), max(n1-1, n2-1))
            if edge in critical_edges:
                return [n1, n2]

        return []