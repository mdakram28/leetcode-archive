class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        piles = [0] + list(itertools.accumulate(piles))

        @cache
        def stones_bob(i, m):
            if i == n: return (0, 0)
            stones = (0, 0)
            for j in range(i+1, min(n, i+2*m)+1):
                alice, bob = stones_alice(j, max(m, j-i))
                bob += piles[j]-piles[i]
                if bob > stones[1]:
                    stones = (alice, bob)
            # print("Bob", i, m, stones)
            return stones

        @cache
        def stones_alice(i, m):
            if i == n: return (0, 0)
            stones = (0, 0)
            for j in range(i+1, min(n, i+2*m)+1):
                alice, bob = stones_bob(j, max(m, j-i))
                alice += piles[j]-piles[i]
                if alice > stones[0]:
                    stones = (alice, bob)
            # print("Alice", i, m, stones)
            return stones
        
        return stones_alice(0, 1)[0]
