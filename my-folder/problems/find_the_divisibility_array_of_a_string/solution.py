class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        rem = 0
        div = []
        for c in word:
            rem = (rem*10 + int(c)) % m
            div.append(1 if rem == 0 else 0)
        
        return div
            