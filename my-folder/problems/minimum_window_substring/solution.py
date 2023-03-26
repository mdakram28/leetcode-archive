class Solution:
    def minWindow(self, s: str, t: str) -> str:
        rem = len(t)
        rem_f = {}
        
        for c in t:
            rem_f[c] = rem_f.get(c, 0) + 1
        
        start = 0
        end = 0
        found = False
        min_range = (0, len(s))
        
        while end < len(s):

            # Increment end
            while end < len(s) and rem > 0:
                c = s[end]
                if c in rem_f:
                    rem_f[c] -= 1
                    if rem_f[c] >= 0:
                        rem -= 1
                end += 1

            # Increment start
            while start < end and (s[start] not in rem_f or rem_f[s[start]] < 0):
                if s[start] in rem_f:
                    rem_f[s[start]] += 1
                start += 1
            
            if rem == 0:
                # print(f"{start=}, {end=}")
                if (end-start) < (min_range[1] - min_range[0]):
                    min_range = (start, end)
                found = True
                while start < end and rem == 0:
                    if s[start] in rem_f:
                        rem_f[s[start]] += 1
                        if rem_f[s[start]] > 0:
                            rem += 1
                    start += 1
        
        return s[min_range[0]: min_range[1]] if found else ""




            