class Solution:
    def splitNum(self, num: int) -> int:
        n1 = 0
        n2 = 0
        
        digs = []
        while num:
            digs.append(num%10)
            num //= 10
        
        digs.sort(reverse=True)
        while digs:
            d = digs.pop()
            if n1 < n2:
                n1 = n1*10 + d
            else:
                n2 = n2*10 + d
        return n1+n2