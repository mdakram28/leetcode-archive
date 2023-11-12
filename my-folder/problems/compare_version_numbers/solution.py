class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        return next(chain((-1 if a<b else 1 for a, b in zip_longest(map(int, v1.split(".")), map(int, v2.split(".")),fillvalue=0) if a!=b),[0]))
        
            
        