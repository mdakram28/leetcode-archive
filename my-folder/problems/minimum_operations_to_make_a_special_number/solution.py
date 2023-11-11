class Solution:
    def minimumOperations(self, num: str) -> int:
        num = num[::-1]
        ans = len(num)-num.count("0")
        
        first0 = None
        second0 = None
        if "0" in num:
            first0 = num.index("0")
            if "0" in num[first0+1:]:
                ans = min(ans, num.index("0", first0+1)-1)
        
        ind5 = num.index("5") if "5" in num else None
        if ind5 is not None:
            if "2" in num[ind5+1:]:
                ans = min(ans, num.index("2", ind5+1)-1)
            if "7" in num[ind5+1:]:
                ans = min(ans, num.index("7", ind5+1)-1)
        
        if first0 is not None:
            if "5" in num[first0+1:]:
                ans = min(ans, num.index("5", first0+1)-1)
        
        return ans