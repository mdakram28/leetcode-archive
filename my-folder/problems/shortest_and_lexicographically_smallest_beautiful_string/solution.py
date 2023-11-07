class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        start = 0
        n = len(s)
        ones = 0
        
        blen = float('inf')
        bpos = []
        
        for end in range(n):
            if s[end] == '1':
                ones += 1
            while ones > k:
                if s[start] == '1':
                    ones -= 1
                start += 1
            while start < end and s[start] == '0':
                start += 1
            # print(start, end, ones)
            if ones == k:
                l = end-start+1
                # print(":::", l, )
                if l < blen:
                    blen = l
                    bpos = [start]
                elif l == blen:
                    bpos.append(start)
        
        if blen == float('inf'):
            return ""
        
        # print(bpos)
        ret = s[bpos[0]:bpos[0]+blen]
        for p in bpos[1:]:
            ret = min(ret, s[p:p+blen])
        return ret
                    
                    
                    
                    