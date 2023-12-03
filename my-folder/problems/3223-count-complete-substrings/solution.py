class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        # is_end = [False]*(n+1)

        # for i in range(1, len(word)):
        #     if abs(ord(word[i]) - ord(word[i-1])) > 2:
        #         is_end[i] = True
        # is_end[n] = True
        
        # Returns true if word[i:i+j] is complete
        def is_complete(i, j):
            pass
        
        numchars = len(set(word))
        ans = 0

        for j in range(1, numchars+1):
            
            f = defaultdict(int)
            l = 0
            for r in range(n+1):
                while len(f) > j or f[word[l]] > k:
                    f[word[l]] -= 1
                    if f[word[l]] == 0:
                        del f[word[l]]
                    l += 1
                # print(f"{j=}, {l=}, {r=}, {f=}")
                if len(f) == j and min(f.values()) == max(f.values()) == k:
                    ans += 1


                if r > 0 and (r == n or abs(ord(word[r]) - ord(word[r-1])) > 2):
                    l = r
                    f = defaultdict(int)

                if r < n:
                    f[word[r]] += 1


        return ans
