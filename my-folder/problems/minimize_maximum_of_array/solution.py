class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = sum(nums)

        rem = 0
        max_val = 0
        for i in range(len(nums)-1, 0, -1):
            target = math.ceil(total/(i+1))
            n = nums[i]
            if n > target:
                rem += n - target
                n = target
            else:
                if n+rem <= target:
                    n += rem
                    rem = 0
                else:
                    rem -= (target-n)
                    n = target
            total -= n
            print(f"{rem=}, {n=}")
            max_val = max(max_val, n)
        
        max_val = max(max_val, nums[0]+rem)

        return max_val