class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        prev = False
        for b in derived:
            if b:
                prev = not prev
        
        return not prev