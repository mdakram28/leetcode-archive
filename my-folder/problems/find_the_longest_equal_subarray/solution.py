class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos = defaultdict(list)
        for i, n in enumerate(nums):
            pos[n].append(i)
        
        ans = 0
        for n, p in pos.items():
            d = 1
            prev = p[0]
            D = []
            l = 0
            for x in p:
                d += x-prev-1
                D.append(d)
                prev = x
                while d-D[l] > k:
                    l += 1
                ans = max(ans, len(D)-l)
        return ans
        