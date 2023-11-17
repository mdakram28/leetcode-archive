class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for i in range(min(len(str1), len(str2)), 0, -1):
            if len(str1)%i != 0 or len(str2)%i != 0: continue
            pref = str2[:i]
            for j in range(0, len(str1), i):
                if str1[j:j+i] != pref:
                    break
            else:
                for j in range(0, len(str2), i):
                    if str2[j:j+i] != pref:
                        break
                else:
                    return pref
        
        return ""