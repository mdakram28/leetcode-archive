class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        neg_inf = float('-inf')
        n = len(nums)
        nums.append(neg_inf)
        nums.append(neg_inf)

        l = 0
        r = n
        while l < r:
            mid = (l+r) // 2
            # print(f"{mid=}")
            n1, n2, n3 = nums[mid-1], nums[mid], nums[mid+1]
            if n2 > n1 and n2 > n3:
                return mid
            elif n1 > n2 > n3:
                # print(f"Moving left")
                r = mid
            else:
                # print(f"Moving right")
                l = mid+1

        return None