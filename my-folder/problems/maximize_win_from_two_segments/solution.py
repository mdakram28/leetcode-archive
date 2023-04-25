class Solution:
    def maximizeWin(self, arr: List[int], k: int) -> int:
        
        dp = []
        
        n = len(arr)

        start = 0
        end = 0
        while end < n and arr[end]-arr[0] <= k:
            end += 1
            dp.append(end)
        
        ans = end-start
        
        while end < n:
            # Remove one from start
            start += 1

            while end < n and arr[end]-arr[start] <= k:
                end += 1
                dp.append(max(dp[-1], end-start))
            
            ans = max(ans, end-start + dp[start-1])


        return ans        
        
        