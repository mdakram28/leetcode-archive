class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], costs: List[int]) -> int:
        cost = defaultdict(dict)
        for a, b, c in zip(original, changed, costs):
            cost[a][b] = min(cost[a].get(b, c), c)
            
        # print(cost)
        alldist = defaultdict(lambda: defaultdict(lambda: float('inf')))
        for start in list(cost.keys()):
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
                        
            # print(start, dist)
        
        # print(alldist)
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            alldist[letter][letter] = 0
        
        ans = sum(alldist[a][b] for a, b in zip(source, target))
        
        return -1 if ans == float('inf') else ans
