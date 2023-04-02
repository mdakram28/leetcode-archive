class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        j = 0
        d = {}
        def check_word(w):
            nonlocal j
            try:
                if j >= len(pattern):
                    return False
                if pattern[j] in d:
                    return d[pattern[j]] == w
                else:
                    d[pattern[j]] = w
                return True
            finally:
                j += 1

        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                if not check_word(s[start:i]):
                    return False
                start = i+1
        
        i += 1
        if not check_word(s[start:i]):
            return False
        
        if j != len(pattern):
            return False

        w = set()
        for word in d.values():
            if word in w:
                return False
            w.add(word)
        
        return True