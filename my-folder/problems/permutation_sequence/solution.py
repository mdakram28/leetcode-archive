class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = []
        rem = [i for i in range(1, n+1)]

        fact = 1
        for i in range(2, n):
            fact *= i
        j = n-1
        k -= 1

        while rem:
            sel = k//fact
            digits.append(rem[sel])
            rem.remove(rem[sel])

            k = k%fact
            if rem:
                fact //= j
                j -= 1
        return ''.join(map(str, digits))