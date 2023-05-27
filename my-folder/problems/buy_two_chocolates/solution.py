class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a, b = float('inf'), float('inf')
        for p in prices:
            if p < a:
                a, b = p, a
            elif p < b:
                b = p
        
        if a+b > money:
            return money
        else:
            return money-(a+b)