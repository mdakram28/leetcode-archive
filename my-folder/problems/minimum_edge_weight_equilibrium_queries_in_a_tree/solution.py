class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = defaultdict(dict)
        fcache = {0: {}}
        level = {}
        g = defaultdict(dict)
        masks = [1<<i for i in range(32)]
        
        for a, b, w in edges:
            g[a][b] = w 
            g[b][a] = w
        
        prev = []
        f = defaultdict(int)
        def assign_parent(at, p):

            prev_dist = 1
            while len(prev) >= prev_dist:
                parent[at][prev_dist] = prev[-prev_dist]
                fcache[at] = {**f}
                prev_dist <<= 1

            prev.append(at)
            level[at] = len(prev)
            for to, w in g[at].items():
                if to == p: continue
                f[w] += 1
                assign_parent(to, at)
                f[w] -= 1
            prev.pop()
        

        assign_parent(0, None)
        

        def goto_level(at, l):
            dist = level[at]-l
            while dist > 0:
                at = parent[at][dist^(dist&(dist-1))]
                dist &= dist-1
            return at
        
        def lca(a, b):
            # print("lca ----", a, b)
            if level[a] < level[b]:
                a, b = b, a
            a = goto_level(a, level[b])
            # print(a, b)
            if a == b:
                return a
            lo = 0
            hi = level[a]
            while lo < hi:
                mid = (lo+hi)//2
                mida, midb = goto_level(a, mid), goto_level(b, mid)
                if mida == midb:
                    lo = mid+1
                else:
                    hi = mid
                    a, b = mida, midb
            return goto_level(a, lo-1)

        ans = []
        for a, b in queries:
            anc = lca(a, b)
            f1 = fcache[a]
            f2 = fcache[b]
            fa = fcache[anc]
            # print(a, b ,anc)
            # print(f1, f2 , fa)
            

            if len(f1) == 0 and len(f2) == 0:
                ans.append(0)
            else:
                ans.append(
                    sum(f1.values()) + sum(f2.values()) - 2*sum(fa.values()) - 
                    max(
                        f1.get(w,0)-2*fa.get(w, 0) + f2.get(w,0)
                        for w in (set(chain(f1.keys(),f2.keys())))
                    )
                )
        
        return ans
