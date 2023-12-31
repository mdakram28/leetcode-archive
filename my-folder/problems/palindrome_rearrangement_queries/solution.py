class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        A = s[:len(s)//2]
        B = s[len(s)//2:][::-1]
        ALL_CHARS = 'abcdefghijklmnopqrstuvwxyz'
        
        diff = list(accumulate(1 if a!=b else 0 for a, b in zip(A, B)))
        diff.append(0)
        
        def same_in_range(l, r):
            return diff[l-1] == diff[r]
        
        
        def get_freq(s):
            f = {c: 0 for c in ALL_CHARS}
            ret = []
            for c in s:
                f[c] += 1
                ret.append({**f})
            ret.append({c: 0 for c in ALL_CHARS})
            return ret
        
        freqa = get_freq(A)
        freqb = get_freq(B)
        
        
        def freq_in_range(d, l, r):
            f1 = d[l-1]
            f2 = d[r]
            return {c: f2[c]-f1[c] for c in ALL_CHARS}
        
        def sub(f1, f2):
            return {c: f1[c]-f2[c] for c in ALL_CHARS}
        
        ans = []
        
        for a,b,c,d in queries:
            c = n-c-1
            d = n-d-1
            
            f1 = freq_in_range(freqa, a, b)
            f2 = freq_in_range(freqb, d, c)
            
            total = 0
            start = 0
            ranges = []
            for pos, added in sorted([(a, 1), (b+1, -1), (d, 2), (c+1, -2), (n//2, 0)]):
                if pos-1 >= start:
                    ranges.append((start, pos-1, total))
                total += added
                start = pos
            
            
            pal = True
            for l, r, count in ranges:
                if count == 0 and not same_in_range(l, r):
                    pal = False
                    break
            if not pal:
                ans.append(False)
                continue
                
            for l, r, count in ranges:
                if count == 1:
                    f1 = sub(f1, freq_in_range(freqb, l, r))
                    if any(f1[c] < 0 for c in ALL_CHARS):
                        pal = False
                        break
                if count == 2:
                    f2 = sub(f2, freq_in_range(freqa, l, r))
                    if any(f2[c] < 0 for c in ALL_CHARS):
                        pal = False
                        break
                        
            if not pal:
                ans.append(False)
                continue
                
            for l, r, count in ranges:
                if count == 3:
                    if any(f1[c] != f2[c] for c in ALL_CHARS):
                        pal = False
                        break
            
            ans.append(pal)
            
            
        
        return ans