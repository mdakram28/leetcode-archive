class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for d in details:
            if int(d[-4:-2]) > 60: count += 1
        return count