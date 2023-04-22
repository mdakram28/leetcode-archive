class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        letters = [None] * n
        curr_l = 'a'
        
        for i in range(n):
            if lcp[i][i] != n-i: return ""
            # for j in range(i+1, n):
            #     if lcp[i][j]
            lcp[i].append(0)
        
        for i in range(n):
            l = letters[i]
            if l is not None:
                for j in range(i+1, n):
                    if lcp[i][j] != lcp[j][i]: return ""
                    if lcp[i][j] and letters[j] != l: return ""
            else:
                if curr_l > 'z': return ""
                for j in range(i, n):
                    if lcp[i][j] != lcp[j][i]: return ""
                    if lcp[i][j]:
                        if letters[j]:
                            if letters[j] != curr_l: return ""
                        else:
                            letters[j] = curr_l
                curr_l = chr(ord(curr_l) + 1)
                
            
        for i in range(n-1):
            for j in range(i+1, n):
                if letters[i] == letters[j] and lcp[i][j]!=lcp[i+1][j+1]+1:
                    return ""
        
        
        return ''.join(letters)
                