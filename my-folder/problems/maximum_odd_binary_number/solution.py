class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        return str("1"*(ones-1) + "0"*(len(s)-ones) + "1")