class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high+1):
            num = str(num)
            n = len(num)
            if len(num)%2 != 0: continue
                
            if sum(map(int, list(num[:n//2]))) == sum(map(int, list(num[n//2:]))):
                count += 1
        
        return count