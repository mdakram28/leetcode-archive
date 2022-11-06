class Solution:
    def findOffset(self, nums):
        l = 0
        r = len(nums)
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        return l+1
    def search(self, nums: list[int], target: int) -> int:
        offset = self.findOffset(nums)
        length = len(nums)
        l = 0
        r = len(nums)
        i  = lambda x: (x+offset)%length

        print("Offset : ", offset)

        while l < r:
            mid = (l+r) // 2
            if nums[i(mid)] < target:
                l = mid+1
            else:
                r = mid
        return i(l) if nums[i(l)] == target else -1