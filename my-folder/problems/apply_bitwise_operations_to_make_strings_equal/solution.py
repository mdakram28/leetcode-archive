class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        num1 = s.count('1')
        
        num01 = sum(1 for a,b in zip(s, target) if a=='0' and b=='1')
        if num01 > 0 and num1 == 0:
            return False
        
        num10 = sum(1 for a,b in zip(s, target) if a=='1' and b=='0')
        num11 = sum(1 for a,b in zip(s, target) if a=='1' and b=='1')
        if num10 > 0 and num01 == 0 and num11 == 0:
            return False
        
        return True
        
        # num1 += sum(1 for a,b in zip(s, target) if a=='0' and b=='1')
        
        # num10 = sum(1 for a,b in zip(s, target) if a=='1' and b=='0')
        
#         if num1 == 0:
#             return 