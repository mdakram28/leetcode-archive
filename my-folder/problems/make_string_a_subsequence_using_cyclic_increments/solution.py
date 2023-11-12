class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1): return False
        i = 0
        j = 0
        
        while i<len(str1) and j<len(str2):
            if str1[i] == str2[j] or chr(ord('a') + ((ord(str1[i])-ord('a'))+1)%26) == str2[j]:
                j += 1
            i += 1
        
        return j == len(str2)