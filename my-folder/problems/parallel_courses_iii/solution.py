class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g = defaultdict(list)
        # is_end = [True] * n
        for a, b in relations:
            g[b-1].append(a-1)
            # is_end[a-1] = False

        @cache
        def endtime(at):
            return max((endtime(to) for to in g[at]), default=0) + time[at]
        
        return max(endtime(at) for at in range(n))