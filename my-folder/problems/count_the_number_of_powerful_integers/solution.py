class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        ints = int(s)
        s = [int(d) for d in s]
        INF = "9999999999999999999999999"
        
        @cache
        def count_pf(dig, i, upto):
            if i == 0: return 1 if dig == s[-1] else 0
            if dig > limit or dig < 0: return 0
            if i < len(s) and dig != s[-i-1]:
                return 0
            
            if dig > int(upto[-i-1]):
                return 0
            
            next_upto_dig = int(upto[-(i-1)-1])
            ans = count_pf(next_upto_dig, i-1, upto)
            for next_dig in range(next_upto_dig-1, -1, -1):
                ans += count_pf(next_dig, i-1, INF)
            
            
            # print(f"{''.join(['    ']*(10-i))}, {i=}, {dig=}, {upto=}, {ans=}")
            return ans
        
        
        def get_count(num):
            if num < ints:
                return 0
            num = str(num)
            # print("num", num)
            ret = count_pf(0, len(num), num.zfill(len(num)+1))
            return ret
        
        start -= 1
        r = get_count(finish)
        l = get_count(start)
        return r - l