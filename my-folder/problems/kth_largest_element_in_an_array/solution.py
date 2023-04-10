class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        left = 0
        right = n-1
        k = n-k
        l = left

        while left <= right:
            l = left
            r = right
            while l<r:
                if nums[l] > nums[r]:
                    nums[r], nums[l], nums[r-1] = nums[l], nums[r-1], nums[r]
                    r -=1
                else:
                    l += 1
            # print(l, nums)
            if k < l:
                right = l-1
            elif k > l:
                left = l+1
            else:
                break

        return nums[l]