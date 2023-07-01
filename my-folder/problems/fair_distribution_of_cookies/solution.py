class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        dist = []
        ans = float('inf')

        def min_unfairness(i):
            nonlocal ans
            if i+1 < k-len(dist):
                return
            if i == -1:
                ans = min(ans, max(dist))
                return
            c = cookies[i]
            for child in range(len(dist)):
                dist[child] += c
                min_unfairness(i-1)
                dist[child] -= c
            if len(dist) < k:
                dist.append(c)
                min_unfairness(i-1)
                dist.pop()
        
        min_unfairness(len(cookies)-1)
        return ans


            