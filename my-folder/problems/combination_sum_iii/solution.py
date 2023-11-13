class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def sigma(l ,r):
            return (r*(r+1))//2 - (l*(l-1))//2
        
        @cache
        def get_all(count, target, lower):
            if count == 1:
                return [[target]]

            count -= 1

            lastnum = min(
                9,
                9-count,
                (2*target-count**2-count)//(2*count+2)
            )
            lower = max(
                lower,
                target-sigma(10-count, 9)
            )
            if lower > lastnum: return []
            ret = []
            # for num in range(lower, lastnum+1):
            for suff in get_all(count, target-lower, lower+1):
                ret.append([lower]+suff)
            ret.extend(get_all(count+1, target, lower+1))
            return ret

        return get_all(k, n, 1)