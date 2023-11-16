class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a,b,c = 0,0,0
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            a = max(a, t[0])
            b = max(b, t[1])
            c = max(c, t[2])
        # print(a,b,c)
        return  [a,b,c] == target