class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0
        for row in bank:
            count = row.count("1")
            if count == 0:
                continue
            ans += count*prev
            prev = count
        return ans