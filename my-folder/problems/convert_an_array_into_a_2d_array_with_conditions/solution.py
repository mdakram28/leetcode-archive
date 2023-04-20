class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] += 1
        ret = [[] for _ in range(max(freq.values()))]
        for num, f in freq.items():
            for r in range(f):
                ret[r].append(num)
        return ret