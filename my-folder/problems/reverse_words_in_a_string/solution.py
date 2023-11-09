class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(filter(lambda w: len(w)>0,reversed(s.split(" "))))