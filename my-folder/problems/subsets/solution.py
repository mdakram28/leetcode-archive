class Solution:
    def addSubsets(self, i: int, l: List[int], s: List[List[int]], nums: List[int]) -> None:
        if i >= len(nums):
            s.append(l.copy())
        else:
            # print(f"{indent}{nums[i]}") 
            self.addSubsets(i+1, l, s, nums)
            l.append(nums[i])
            self.addSubsets(i+1, l, s, nums)
            l.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s = []
        self.addSubsets(0, [], s, nums)
        return s