class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        count = [1]*10

        for _ in range(n-1):
            count = [sum(count[num2] for num2 in moves[num])%(10**9+7) for num in range(10)]
        
        return sum(count)%(10**9+7)
