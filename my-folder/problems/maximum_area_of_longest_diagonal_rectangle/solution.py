class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return max((l*l+w*w, l*w) for l, w in dimensions)[1]