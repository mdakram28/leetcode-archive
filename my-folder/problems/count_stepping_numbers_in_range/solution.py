class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        mod = 10**9+7
        NEXT_OPTS = []
        for i in range(10):
            opts = []
            if i-1 >= 0: opts.append(i-1)
            if i+1 <= 9: opts.append(i+1)
            NEXT_OPTS.append(opts)
        
        LIMITS = [[9]*max(len(low)+1, len(high)+1)]
        
        def digitat(limitid, pos):
            return LIMITS[limitid][-pos]
        
        @cache
        def getways(digit: int, count: int, limitid: int):
            if count == 1: return 1
            ans = 0
            for nextd in NEXT_OPTS[digit]:
                # print(nextd, digitat(limitid, count-1))
                if nextd > digitat(limitid, count-1):
                    continue
                elif nextd == digitat(limitid, count-1):
                    ans = (ans + getways(nextd, count-1, limitid))%mod
                else:
                    ans = (ans+getways(nextd, count-1, 0))%mod
            # print(f"{digit=}, {count=}, {LIMITS[limitid]=}, {ans=}")
            return ans
        
        def count_nums(maxnum: str):
            if maxnum == "0": return 0
            limitid = len(LIMITS)
            digits = [int(d) for d in maxnum]
            LIMITS.append(digits)
            maxdigit = digits[0]
            # print(digits)
            ans = (sum(getways(d, len(digits), 0) for d in range(1, maxdigit)) + getways(maxdigit, len(digits), limitid))%mod
            for count in range(1, len(digits)):
                ans = (ans+sum(getways(d, count, 0) for d in range(1, 10)))%mod
            # print(maxnum, ans)
            return ans
        
        
        return (count_nums(high) - count_nums(str(int(low)-1)))%mod
                
                