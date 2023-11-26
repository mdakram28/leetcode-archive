class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        counts = [{} for _ in range(len(nums))]
        total = 0
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in counts[j]:
                    # print(counts[j], counts[j][diff], j, i)
                    total += counts[j][diff]
                counts[i][diff] = counts[i].get(diff, 0) + counts[j].get(diff, 0) + 1
        
        return total