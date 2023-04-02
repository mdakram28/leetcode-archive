class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        
        total = [0]
        t = 0
        for i in range(len(nums)):
            t += nums[i]
            total.append(t)
        
        op = []
        for q in queries:
            
            l = 0
            r = len(nums)
            while l < r:
                mid = (l+r) // 2
                if nums[mid] < q:
                    l = mid+1
                else:
                    r = mid
            
            left_sum = total[l]
            right_sum = total[-1] - total[l]
            
            op.append( (q*l - left_sum) + (right_sum - q*(len(nums)-l)))
        
        return op
            