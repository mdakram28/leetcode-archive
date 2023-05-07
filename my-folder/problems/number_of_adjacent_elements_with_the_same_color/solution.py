class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = [0]*(n+1)
        
        ans = []
        diff = 0
        for i, col in queries:
            if col == arr[i]:
                ans.append(diff)
                continue
            if arr[i] != 0:
                if arr[i] == arr[i-1]:
                    diff -= 1
                if arr[i] == arr[i+1]:
                    diff -= 1
            arr[i] = col
            if arr[i] == arr[i-1]:
                diff += 1
            if arr[i] == arr[i+1]:
                diff += 1
            ans.append(diff)
        return ans
                    