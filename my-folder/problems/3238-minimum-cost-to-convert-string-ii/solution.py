class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], costs: List[int]) -> int:
        cost = defaultdict(dict)
        nodeid = {}
        for a, b, c in zip(original, changed, costs):
            a = nodeid.setdefault(a, len(nodeid))
            b = nodeid.setdefault(b, len(nodeid))
            cost[a][b] = min(cost[a].get(b, c), c)
            
        n = len(nodeid)
        
        alldist = [[float('inf')]*n for _ in range(n)]
        for start in range(n):
            dist = alldist[start]
            q = [(0, start)]
            dist[start] = 0
            while q:
                _, at = heappop(q)
                for to, d in cost[at].items():
                    d2 = dist[at] + d
                    if d2 < dist[to]:
                        dist[to] = d2
                        heappush(q, (d2, to))
        
        
        root = {}
        for word, at in nodeid.items():
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node["$"] = at
        
        # print(root)
        
        @cache
        def get_min_cost(i):
            if i == len(source):
                return 0
            snode = root
            tnode = root
            j = i
            ans = float('inf') if source[i] != target[i] else get_min_cost(i+1)
            while j < len(source) and snode is not None and tnode is not None:
                snode = snode.get(source[j])
                tnode = tnode.get(target[j])
                if snode is not None and "$" in snode and tnode is not None and "$" in tnode:
                    sat = snode["$"]
                    tat = tnode["$"]
                    # print("Match", i, j, alldist[sat][tat])
                    if alldist[sat][tat] != float('inf'):
                        ans = min(ans, alldist[sat][tat] + get_min_cost(j+1))
                j += 1
            
            return ans
            
            
            
                
        ans = get_min_cost(0)
        return -1 if ans == float('inf') else ans
