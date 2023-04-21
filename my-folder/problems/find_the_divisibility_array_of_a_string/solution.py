class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        rem = 0
        for d in word:
            rem = (rem*10 + int(d))%m
            ans.append(int(rem == 0))
        return ans