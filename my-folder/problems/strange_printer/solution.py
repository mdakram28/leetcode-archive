class Solution:
    def strangePrinter(self, s: str) -> int:
        chars = []
        prev = s[0]
        for c in s:
            if c == prev:
                continue
            chars.append(prev)
            prev = c
        chars.append(prev)

        # Returns minimum turns to print all from [l, r)
        @cache
        def get_turns(l, r):
            if l >= r: return 0
            ans = 1 + get_turns(l+1, r)
            for mid in range(l+1, r):
                if chars[mid] != chars[l]: continue
                ans = min(ans, get_turns(l+1, mid+1) + get_turns(mid+1, r))
            return ans

        # return recur(''.join(chars))
        return get_turns(0, len(chars))