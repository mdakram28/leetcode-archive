class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        occ = set(nums)
        for a, b in zip(moveFrom, moveTo):
            if a in occ:
                occ.remove(a)
                occ.add(b)
        
        return list(sorted(list(occ)))