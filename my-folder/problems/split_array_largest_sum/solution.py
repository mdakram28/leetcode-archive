class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lo = max(nums)
        n = len(nums)
        nums.append(0)
        for i in range(n):
            nums[i] += nums[i-1]

        def get_num_sets(t):
            sets = 0

            lo = 0
            while lo < n:
                sets += 1
                target = nums[lo-1]+t
                hi = n
                while lo<hi:
                    mid = (lo+hi)//2
                    if nums[mid] <= target:
                        lo = mid+1
                    else:
                        hi = mid
            # print(f"{t=}, {sets=}")
            return sets


        hi = nums[-2]
        while lo < hi:
            mid = (lo+hi)//2
            if get_num_sets(mid) > k:
                lo = mid + 1
            else:
                hi = mid

        return lo


