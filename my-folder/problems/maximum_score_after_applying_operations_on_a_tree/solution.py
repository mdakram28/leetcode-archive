class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        @cache
        def sumChildren(at, p):
            return sum(values[to] + sumChildren(to, at) for to in g[at] if to != p)
        
        def getMaxScore(at, p):
            if len(g[at]) == 1 and at != 0:
                return 0
            score_taken = values[at] + sum(getMaxScore(to, at) for to in g[at] if to != p)
            score_nottaken = sumChildren(at, p)
            # print(f"{at=}, {score_taken=}, {score_nottaken=}")
            return max(score_taken, score_nottaken)
        
        # for at in g.keys():
        #     print(at, g[at])
        return getMaxScore(0, None)
        