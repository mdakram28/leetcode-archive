class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        
        # dp = {}
        
#         def to_make(x):
#             if x == y: return 0
#             if x < y-60 or x > y+60: return float('inf')
            
#             if x in dp:
#                 return dp[x]
#             dp[x] = float('inf')
            
#             ans = float('inf')
#             ans = min(ans, 1+to_make(x-1), 1+to_make(x+1))
#             if x%11 == 0:
#                 ans = min(ans, 1+to_make(x//11))
#             if x%5 == 0:
#                 ans = min(ans, 1+to_make(x//5))
            
#             dp[x] = ans
#             return ans
        
        
        
        # ans = to_make(x)
        # print(dp)
        # return ans
        dist = {}
        q = deque([(0, x)])
        while True:
            d, at = q.popleft()
            if at == y:
                return d
            to = [at+1, at-1]
            if at%11 == 0:
                to.append(at//11)
            if at%5 == 0:
                to.append(at//5)
            
            for dest in to:
                if dest not in dist:
                    dist[dest] = d+1
                    q.append((d+1, dest))
            
        