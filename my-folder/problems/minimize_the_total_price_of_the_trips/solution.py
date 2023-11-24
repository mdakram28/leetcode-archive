class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        value = defaultdict(int)

        def find(at, p, f):
            value[at] += price[at]
            if at == f: return True
            for to in g[at]:
                if to == p: continue
                if find(to, at, f):
                    return True
            value[at] -= price[at]
            return False

        for start, end in trips:
            find(start, None, end)
        
        # print(value)

        @cache
        def maxTotal(at, p, half: bool):
            ans = value[at]
            if half:
                ans //= 2
            for to in g[at]:
                if to == p: continue
                if half:
                    ans += maxTotal(to, at, False)
                else:
                    ans += min(maxTotal(to, at, False), maxTotal(to, at, True))
            # print(at, half, ans)
            return ans

        ans = min(maxTotal(0, None, True), maxTotal(0, None, False))
        return -1 if ans == float('inf') else ans