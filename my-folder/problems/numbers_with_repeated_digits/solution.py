class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        totaldigits = len(str(n))

        @cache
        def count(digits: int, limit: bool, taken: int):
            total = 0
            if digits == 0:
                return 1
            elif not limit:
                for taked in range(10):
                    if taken & (1<<taked): continue
                    nexttaken = taken | ((1 if taken != 0 or taked != 0 else 0) << taked)
                    total += count(digits-1, False, nexttaken)
            else:
                lastd = (n//(10**(digits-1)))%10
                for taked in range(lastd+1):
                    if taken & (1<<taked): continue
                    nexttaken = taken | ((1 if taken != 0 or taked != 0 else 0) << taked)
                    nextlimit = taked == lastd
                    total += count(digits-1, nextlimit, nexttaken)
            return total
            
        return n-count(totaldigits, True, 0)+1