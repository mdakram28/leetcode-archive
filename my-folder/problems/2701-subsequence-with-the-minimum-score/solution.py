class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        l = 0
        r = len(t)-1
        rind = []

        for i in range(len(s)-1, -1, -1):
            if t[r] == s[i]:
                r -= 1
                rind.append(i)
            if r < 0:
                break
        
        ans = r-l+1
        # mid: last l
        for mid in range(len(s)):
            if l<len(t) and s[mid] == t[l]:
                l += 1
            if rind and mid == rind[-1]:
                r += 1
                rind.pop()
            # print(f"{mid=}, {l=}, {r=}")
            if r-l+1 >= 0:
                ans = min(ans, r-l+1)
        
        return ans

            

