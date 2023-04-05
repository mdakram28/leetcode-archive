class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(list(filter(bool, s.split(" ")))))