class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        f = defaultdict(int)
        for c in magazine:
            f[c] += 1
        for c in ransomNote:
            if f[c] == 0: return False
            f[c] -= 1
        
        return True