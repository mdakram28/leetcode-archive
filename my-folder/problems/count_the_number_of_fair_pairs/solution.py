class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        total = 0
        for i in range(n-1):
            t = lower-nums[i]
            
            l = i+1
            r = n
            while l<r:
                mid = (l+r)//2
                if nums[mid] < t:
                    l = mid+1
                else:
                    r = mid
            left = l
            
            t = upper-nums[i]
            l = left
            r = n
            while l<r:
                mid = (l+r)//2
                if nums[mid] <= t:
                    l = mid+1
                else:
                    r = mid
            right = l
            total += right-left
        return total
            