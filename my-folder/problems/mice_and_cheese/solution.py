class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        diff = sorted(
            (reward2[i]-reward1[i], i)
            for i in range(n)
        )
        total = sum(reward2)
        for _, i in diff[:k]:
            total -= reward2[i] - reward1[i]
        return total
        