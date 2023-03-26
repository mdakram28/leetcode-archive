class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = (digits[-1] + 1) // 10
        digits[-1] = (digits[-1] + 1)%10

        i = len(digits)-2
        while c > 0 and i >= 0:
            s = digits[i] + c
            digits[i] = s%10
            c = s//10
            i-=1
        # print(f"{digits=}, {c=}")
        if c > 0:
            digits.insert(0, c)
        return digits