class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        total_servers = n
        n = len(logs)
        logs.sort(key=lambda l: l[1])
        
        l, r = 0, 0
        count = {}
        ans = [0]*len(queries)
        
        for t, qi in sorted((t, i) for i, t in enumerate(queries)):
            
            while r < n and logs[r][1] <= t:
                count[logs[r][0]] = count.get(logs[r][0], 0) + 1
                r += 1
            
            while l<r and logs[l][1] < (t-x):
                sid, t2 = logs[l]
                count[sid] -= 1
                if count[sid] == 0:
                    del count[sid]
                l += 1
            # print(t, count)
            ans[qi] = total_servers - len(count)
        
        return ans