class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        diff = 0
        diffdiff = defaultdict(int)
        for i, num in enumerate(nums):
            diff += diffdiff[i]
            # print(i, diff, diffdiff, num+diff)
            if num + diff < 0:
                return False
            if num + diff > 0:
                if i+k > len(nums): return False
                diffdiff[i+k] = num+diff
                diff -= num+diff
        return True