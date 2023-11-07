class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        # DP[i] : longest upto i
        DP = [1] * n
        prev = [-1] * n
        
        @cache
        def isOneDist(a, b):
            changed = 0
            for p, q in zip(words[a], words[b]):
                if p != q:
                    changed += 1
                if changed > 1:
                    return False
            return changed == 1
        
        for i in range(n):
            
            for j in range(i):
                if groups[i] == groups[j] or len(words[i]) != len(words[j]):
                    continue
                if not isOneDist(i, j):
                    continue
                if DP[j] + 1 > DP[i]:
                    DP[i] = DP[j] + 1
                    prev[i] = j
                    
        # print(DP)
        
        end = max(DP)
        end_pos = DP.index(end)
        
        at = end_pos
        ret = [words[at]]
        while (at := prev[at]) != -1:
            ret.append(words[at])
        ret.reverse()
        
        return ret
        