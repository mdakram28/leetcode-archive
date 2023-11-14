class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = set()
        right = defaultdict(int)
        left = defaultdict(int)

        for c in s:
            right[c] += 1
        
        for c in s:
            right[c] -= 1

            for c2 in left.keys():
                if right[c2] > 0:
                    ans.add(c+c2)

            left[c] += 1

        return len(ans)