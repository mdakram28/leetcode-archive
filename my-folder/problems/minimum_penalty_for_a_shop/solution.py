class Solution:
    def bestClosingTime(self, customers: str) -> int:
        leftN = 0
        rightY = customers.count('Y')
        
        min_pen = rightY
        min_i = 0
        
        for i, c in enumerate(customers):
            if c == 'Y':
                rightY -= 1
            else:
                leftN += 1
                
            pen = leftN + rightY
            if pen < min_pen:
                min_pen = pen
                min_i = i+1
        
        return min_i