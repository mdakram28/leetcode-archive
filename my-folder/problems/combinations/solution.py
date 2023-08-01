class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        prev = []
        ans = []

        def add_one(last):
            if len(prev) == k:
                ans.append([*prev])
                return
            for num in range(last+1, n+1):
                prev.append(num)
                # taken[num] = True
                add_one(num)
                prev.pop()
                # taken[num] = False
        
        add_one(0)
        return ans
