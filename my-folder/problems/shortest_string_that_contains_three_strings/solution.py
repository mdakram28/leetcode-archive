@cache
def longest_match(haystack, needle):
    i = 1
    j = 0
    lps = [0]*len(needle)
    while i < len(needle):
        if needle[i] == needle[j]:
            # prevlps += 1
            lps[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                lps[i] = 0
                i += 1
            else:
                j = lps[j-1]
    # print(lps)
    i = 0
    j = 0
    fullmatch = False
    while i < len(haystack):
        if j<len(needle) and haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == len(needle):
                fullmatch = True
        elif j > 0:
            j = lps[j-1]
        else:
            i = i+1
    print(haystack, needle)
    print(j, fullmatch)
    return j if not fullmatch else len(needle)
        
class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        
        def join(a, b, c):
            ans = a + b[longest_match(a, b):]
            ans = ans + c[longest_match(ans, c):]
            return ans
        
        ans = []
        for perm in permutations([a, b, c]):
            s = join(*perm)
            if len(ans) == 0:
                ans.append(s)
            elif len(s) < len(ans[-1]):
                ans = [s]
            elif len(s) == len(ans[-1]):
                ans.append(s)
        return min(ans)
            
            
        