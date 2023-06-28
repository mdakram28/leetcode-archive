class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = [[] for _ in range(n)]
        for (a, b), s in zip(edges, succProb):
            g[a].append((b,s))
            g[b].append((a,s))
        
        q = [start]
        prob = [0]*n
        prob[start] = -1
        for at in q:
            for to, s in g[at]:
                p2 = prob[at]*s
                if p2 < prob[to]:
                    prob[to] = p2
                    q.append(to)
        
        return -prob[end]