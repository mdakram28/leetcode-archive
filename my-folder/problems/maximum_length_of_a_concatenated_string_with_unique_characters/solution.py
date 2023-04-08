class Solution:
    def maxLength(self, arr: List[str]) -> int:
        bits = []

        for word in arr:
            b = 0
            for c in word:
                mask = 1<<(ord(c)-ord('a'))
                if b&mask:
                    b = 0
                    break
                b |= mask
            bits.append(b)

        # d = {}
        @cache
        def max_length(i, taken, l):
            if i == len(arr):
                return l
            # k = (i, taken)
            # if k in d:
            #     return d[k]
            if bits[i]==0 or bits[i]&taken:
                ret = max_length(i+1, taken, l)
            else:
                ret = max(max_length(i+1, taken, l), max_length(i+1, taken | bits[i], l+len(arr[i])))
            # d[k] = ret
            return ret
        
        return max_length(0, 0, 0)