class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return max((v, k) for k, v in Counter(arr).items())[1]
