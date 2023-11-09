class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return sum(((k-1)>>i)&1 for i in range(30))%2
