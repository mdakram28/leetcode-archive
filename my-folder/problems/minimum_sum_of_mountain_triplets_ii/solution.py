class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        minRight = []
        m = float('inf')
        for num in nums[::-1]:
            minRight.append(m)
            m = min(m, num)
        
        minRight.reverse()
        
        minLeft = float('inf')
        ans = float('inf')
        for i, num in enumerate(nums):
            # print(i ,minLeft, num, minRight[i])
            if minLeft < num and minRight[i] < num:
                ans = min(ans, minLeft + num + minRight[i])
            minLeft = min(minLeft, num)
        
        return -1 if ans == float('inf') else ans