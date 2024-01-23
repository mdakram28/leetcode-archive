class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        forb = [0]*n
        lens = [len(w) for w in arr]
        arr = list(map(set, arr))
        
        for i in range(n):
            if lens[i] != len(arr[i]):
                forb[i] = 1 << i

        for i in range(n):
            for j in range(i+1, n):
                if any(c in arr[i] for c in arr[j]):
                    forb[i] |= 1 << j
                    forb[j] |= 1 << i
        
        ans = 0
        for num in range(1 << n):
            if any(num&(1 << i) and forb[i]&num for i in range(n)):
                continue
            ans = max(ans, sum(lens[i] for i in range(n) if num&(1<<i)))
        
        return ans