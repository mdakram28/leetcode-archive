class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        f = defaultdict(int)
        # pairs = defaultdict(int)
        pc = 0
        ans = 0
        
        end = 0
        for start in range(n):
            while end < n and pc+f[nums[end]] < k:
                pc += f[nums[end]]
                f[nums[end]] += 1
                end += 1
            if end == n:
                break
            ans += n-end
            
            f[nums[start]] -= 1
            pc -= f[nums[start]]
        
        return ans