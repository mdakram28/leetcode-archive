class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        # start_loc = locations[start]
        # fin_loc = locations[finish]
        # locations.sort()
        # start = locations.index(start_loc)
        # finish = locations.index(fin_loc)
        n = len(locations)
        mod = 10**9 + 7

        @cache
        def num_paths(i, f):
            if f < 0: return 0
            
            ways = 1 if i == finish else 0
            at = locations[i]
            for j in range(n):
                if j == i: continue
                ways = (ways + num_paths(j, f - abs(locations[j]-at)))%mod
            
            return ways
        
        return num_paths(start, fuel)
