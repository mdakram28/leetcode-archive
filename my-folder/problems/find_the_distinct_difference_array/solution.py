class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        dist = []
        seen = set()
        count = 0
        for num in nums[::-1]:
            if num not in seen:
                seen.add(num)
                count += 1
            dist.append(count)
        
        dist.reverse()
        dist.append(0)
        
        seen = set()
        count = 0
        ans = []
        for i, num in enumerate(nums):
            if num not in seen:
                seen.add(num)
                count += 1
            ans.append(count - dist[i+1])
        return ans