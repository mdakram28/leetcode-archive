class Solution:
    def partition(self, s: str) -> List[List[str]]:
        prev = []
        ret = []
        n = len(s)
        
        @cache
        def is_palindrome(l, r):
            if l >= r: return True
            return s[l] == s[r] and is_palindrome(l+1, r-1)
        
        def add_all(i):
            if i == n:
                ret.append([*prev])
            for j in range(i, n):
                if is_palindrome(i, j):
                    prev.append(s[i:j+1])
                    add_all(j+1)
                    prev.pop()
        
        add_all(0)
        return ret