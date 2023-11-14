class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0
        t = 0
        for i in count(1):
            t += i
            if t > n:
                break
            if (n-t)%i == 0 and (n-t)//i + 1 >= 1:
                ans += 1
        return ans
            