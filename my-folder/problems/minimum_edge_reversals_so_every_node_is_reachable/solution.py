class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for a, b in edges:
            # connection, can_go
            g[a].append((b, True))
            g[b].append((a, False))
        
        num_rev = [0] * n
        
        def calc_child(at, p):
            for to, can_go in g[at]:
                if to == p: continue
                calc_child(to, at)
                num_rev[at] += num_rev[to] + int(not can_go)
        
        def calc_parent(at, p, prev_total):
            num_rev[at] += prev_total
            for to, can_go in g[at]:
                if to == p: continue
                calc_parent(to, at, num_rev[at]-num_rev[to]-int(not can_go) + int(can_go))
            
        
        calc_child(0, -1)
        calc_parent(0, -1, 0)
        
        
        return num_rev