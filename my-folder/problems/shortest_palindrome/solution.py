def strstr(h, n):
    # print(h)
    # print(n)
    if len(n) == 0: return 0
    lps = [0]*len(n)
    i, j = 1, 0

    while i<len(n):
        if n[i] == n[j]:
            lps[i] = j+1
            j += 1
            i += 1
        elif j == 0:
            lps[i] = 0
            i += 1
        else:
            j = lps[j-1]
    # print(lps)
    i = 0
    j = 0
    while j < len(h):
        # print(j,i)
        if h[j] == n[i]:
            i += 1
            j += 1
        elif i == 0:
            j += 1
        else:
            i = lps[i-1]
    return i
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)

        l = strstr(s[::-1], s)
        # print(l)
        return s[l:][::-1]+s

        # def is_pal(l, r):
        #     while l<r:
        #         if s[l] != s[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True
        
        # return ""