class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        maxi = -1
        maxv = ''
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                if num[i] > maxv:
                    maxv = num[i]
                    maxi = i
        
        return maxv+maxv+maxv
