class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        d1 = ""
        for i in range(len(number)):
            if number[i] != digit: continue
            s = number[:i] + number[i+1:]
            if s > d1:
                d1 = s
        return d1