class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustees = collections.defaultdict(int)
        trusts = collections.defaultdict(int)

        for p1, p2 in trust:
            trustees[p2] += 1
            trusts[p1] += 1
        
        judge = None
        for i in range(1, n+1):
            if trustees[i] != (n-1) or trusts[i] != 0:
                continue
            if judge:
                return -1
            judge = i
        return judge or -1