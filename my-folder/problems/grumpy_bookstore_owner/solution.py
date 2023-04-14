class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)

        start = 0
        end = 0
        g = 0
        while end < minutes:
            g += customers[end] * grumpy[end]
            end += 1
        
        max_g = g

        while end < n:
            g += customers[end] * grumpy[end]
            g -= customers[start] * grumpy[start]
            end += 1
            start += 1

            max_g = max(max_g, g)
        
        return sum(customers[i]*(1-grumpy[i]) for i in range(n)) + max_g