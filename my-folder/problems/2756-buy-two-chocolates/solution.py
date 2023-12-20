class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        fs,ss=101,101
        for i in prices :
            if i<fs:
                ss=fs
                fs=i
        
            elif i<ss :
                ss=i 
        if (fs+ss)>money :
            return money
        return money-(fs+ss)
