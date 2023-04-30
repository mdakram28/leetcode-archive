class Solution:
    def findLucky(self, arr: List[int]) -> int:
        f = defaultdict(int)
        for num in arr:
            f[num] += 1
        
        ans = -1
        for num, val in f.items():
            if num == val:
                ans = max(ans, num)
        
        return ans