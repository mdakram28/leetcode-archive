import inspect
from functools import wraps

def dump_args(func):
    """
    Decorator to print function call details.

    This includes parameters names and effective values.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        func_args = inspect.signature(func).bind(*args, **kwargs).arguments
        func_args_str = ", ".join(map("{0[0]} = {0[1]!r}".format, func_args.items()))
        ret = func(*args, **kwargs)
        print(f"({func_args_str}) => {ret}")
        return ret

    return wrapper

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        group, profit = zip(*sorted(zip(group, profit)))
        mod = 10**9+7

        # @cache
        # # @dump_args
        # def num_ways(i, n, p):
        #     '''
        #     i: Max index of crime
        #     n: Num of people
        #     '''
        #     if i == -1 or n == 0: return 1 if p <= 0 else 0
        #     return (num_ways(i-1, n, p) + (
        #         num_ways(i-1, n-group[i], p-profit[i])
        #         if group[i] <= n else 0
        #     )) % mod

        dp = [[1]*(n+1)] + [[0]*(n+1) for i in range(minProfit)]
        # dp[p][n] => ways to make at least p profit using n members

        for i in range(len(group)):
            # dp_curr[p][n] = dp_prev[p][n] + dp_prev[p-profit[i]][n-group[i]]
            for p in range(minProfit, -1, -1):
                for n2 in range(n, group[i]-1, -1):
                    # if group[i] > n2: break
                    dp[p][n2] = (dp[p][n2] + dp[max(p-profit[i], 0)][n2-group[i]]) % mod
            # print(f"---------- {i=}, {group[i]}, {profit[i]}")
            # print('\n'.join(map(str, dp)))

        
        return dp[-1][-1]
















