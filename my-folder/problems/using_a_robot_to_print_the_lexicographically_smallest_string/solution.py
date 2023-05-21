from sortedcontainers import SortedList

class Solution:
    def robotWithString(self, s: str) -> str:
        ans = []
        
        t = []
        n = len(s)
        sl = SortedList()
        
        for i in range(n):
            sl.add((s[i], i))
        
        i = 0
        while sl:
            # print(t, sl)
            min_char, min_i = sl[0]
            if t and t[-1] <= min_char:
                ans.append(t.pop())
            else:
                for j in range(i, min_i+1):
                    t.append(s[j])
                    sl.remove((s[j], j))
                i = min_i+1
                    
        while t:
            ans.append(t.pop())
        
        return "".join(ans)