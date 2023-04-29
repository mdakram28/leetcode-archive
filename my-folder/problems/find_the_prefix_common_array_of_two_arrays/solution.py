class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        x = defaultdict(int)
        y = defaultdict(int)
        ans = []
        count = 0
        for a,b in zip(A, B):
            if a == b and (x[a] == 0 or y[b] == 0):
                count += 1
            else:
                if y[b] == 0 and x[b]:
                    count += 1
                if x[a] == 0 and y[a]:
                    count += 1
            x[a] += 1
            y[b] += 1
            ans.append(count)
        
        return ans