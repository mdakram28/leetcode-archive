class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for a, b in adjacentPairs:
            g[a].append(b)
            g[b].append(a)
        
        start = None
        for at, to in g.items():
            if len(to) == 1:
                start = at
        
        at = start
        prev = None
        arr = []

        while True:
            arr.append(at)
            for to in g[at]:
                if to == prev: continue
                prev, at = at, to
                break
            else:
                break
        return arr
