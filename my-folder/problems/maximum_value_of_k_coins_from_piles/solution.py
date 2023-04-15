# Define a class Solution to hold the function.
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # Preprocess the piles to get the prefix sum of each pile.
        for p in piles:
            # Append 0 at the end of all piles to handle edge cases.
            p.append(0)
            # Compute the prefix sum for each pile.
            for i in range(len(p)-1):
                p[i] += p[i-1]

        # Define a constant for infinity.
        INF = float('inf')
        
        # Define a memoized recursive function to find the maximum value of coins.
        @cache
        def max_sum(r, k):
            # Base case: if we are at the first pile, return the sum of the first k coins (if available).
            if r == 0:
                return piles[0][k-1] if k<=len(piles[0]) else -INF
            
            # Initialize a variable to hold the maximum value of coins we can have.
            ret = 0
            # Iterate over all possible number of coins we can take from the current pile.
            for i in range(min(k+1, len(piles[r]))):
                # Recursively compute the maximum value of coins we can have by taking i coins from the current pile
                # and adding it to the maximum value of coins we can have by taking k-i coins from the previous piles.
                ret = max(ret, max_sum(r-1, k-i) + piles[r][i-1])
            return ret

        # Call the recursive function on the last pile to get the maximum value of coins we can have.
        return max_sum(len(piles)-1, k)
