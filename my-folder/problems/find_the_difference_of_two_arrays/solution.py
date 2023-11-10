class Solution:
    def findDifference(self, a: List[int], b: List[int]) -> List[List[int]]:
        a=set(a)
        b=set(b)
        return [a-b,b-a]