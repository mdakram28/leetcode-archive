class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        group = [0] * n
        hates = [[] for p in range(n)]

        for p1, p2 in dislikes:
            hates[p1-1].append(p2-1)
            hates[p2-1].append(p1-1)

        def can_assign(p, g):
            if group[p]:
                return group[p] == g
            group[p] = g
            for h in hates[p]:
                if not can_assign(h, 3-g):
                    return False
            return True

        for p in range(n):
            if group[p] == 0 and not can_assign(p, 1):
                return False
        
        return True
