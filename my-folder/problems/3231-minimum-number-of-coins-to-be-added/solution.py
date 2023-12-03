class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        lim = 0
        count = 0
        i = 0
        while lim < target:
            # print(i, lim, count)
            if i < len(coins) and lim >= (coins[i]-1):
                lim += coins[i]
                i += 1
                continue
            
            count += 1
            lim += lim+1
        
        return count
        
