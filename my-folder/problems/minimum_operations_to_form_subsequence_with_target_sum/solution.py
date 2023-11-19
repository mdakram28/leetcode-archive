class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        heapify(nums)
        splits = 0
        while nums and target:
            needed = target^(target&(target-1))
            # print(st, needed)
            found = heappop(nums)
            if needed == found:
                target &= ~found
            elif found > needed:
                splits += 1
                heappush(nums,found//2)
                heappush(nums,found//2)
            elif nums and nums[0] == found:
                heappush(nums, heappop(nums)*2)
        
        return splits if target == 0 else -1
