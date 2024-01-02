class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        ret = []

        for val in nums:
            i = count[val]
            count[val] += 1
            if i >= len(ret):
                ret.append([])
            ret[i].append(val)
        
        return ret