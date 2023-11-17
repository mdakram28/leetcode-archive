class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [c for c in s if c.lower() in 'aeiou']
        return ''.join(c if c.lower() not in 'aeiou' else vowels.pop() for c in s)