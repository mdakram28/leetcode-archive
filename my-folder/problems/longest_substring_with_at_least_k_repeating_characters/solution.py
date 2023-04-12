class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # f = collections.defaultdict(int)
        n = len(s)
        ret = 0

        for max_uniq in range(1, 27):
            start, end = 0, 0
            f = collections.defaultdict(int)
            uniq = 0
            count_k = 0

            while end < n:
                while end < n and (uniq < max_uniq or f[s[end]]):
                    if f[s[end]] == 0:
                        uniq += 1
                    f[s[end]] += 1
                    if f[s[end]] == k:
                        count_k += 1
                    end += 1
                # print(max_uniq, start, end, ' '*start + s[start:end] + ' '*(n-end))
                if count_k == uniq == max_uniq:
                    ret = max(ret, end-start)
                
                if f[s[start]] == k:
                    count_k -= 1
                f[s[start]] -= 1
                if f[s[start]] == 0:
                    uniq -= 1
                start += 1
            
        return ret