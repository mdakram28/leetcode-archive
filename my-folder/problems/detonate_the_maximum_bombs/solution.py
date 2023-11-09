class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        g = defaultdict(list)
        n = len(bombs)

        def can_det(b1, b2):
            return (b1[0]-b2[0])**2 + (b1[1]-b2[1])**2 <= b1[2]**2

        for b1 in range(n):
            for b2 in range(n):
                if b1 != b2 and can_det(bombs[b1], bombs[b2]):
                    g[b1].append(b2)
        
        allvisited = set()
        visited = set()

        def getMaxDet(at):
            visited.add(at)
            return 1 + sum(getMaxDet(to) for to in g[at] if to not in visited)
        
        ans = 0
        for at in range(n):
            if at in allvisited: continue
            visited.clear()
            ans = max(ans, getMaxDet(at))
            allvisited.update(visited)
        # print(totals, g)
        return ans

