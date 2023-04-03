from heapq import heappush, heappop
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        def dfs(idx):
            if idx == len(nums):
                self.count += 1
                return
            num = nums[idx]
            # Take idx
            if illegal[num] == 0:
                illegal[num-k] += 1
                illegal[num+k] += 1
                dfs(idx+1)
                illegal[num-k] -= 1
                illegal[num+k] -= 1
            
            # Dont take idx
            dfs(idx+1)
        
        
        illegal = collections.defaultdict(int)
        self.count = 0
        dfs(0)
        return self.count - 1
        
        
        
        
        
        