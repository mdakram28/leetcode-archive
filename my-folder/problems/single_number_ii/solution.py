class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = [0]*40

        for n in nums:
            if n < 0: n = -n + 2**32
            for i,b in enumerate(reversed(bin(n))):
                if b == "1":
                    ones[i] += 1
        ones = ["1" if c%3 else "0" for c in ones]
        ones.reverse()
        ans = int("".join(ones), 2)
        return ans if ans < 2**32 else 2**32-ans