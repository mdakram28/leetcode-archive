class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        pos = {}
        n = len(s)
        for i in range(n):
            if s[i] == '0':
                if 0 not in pos:
                    pos[0] = i
                continue
            num = 0
            for j in range(i, min(i+32, n)):
                if s[j] == '1': num = (num<<1) | 1
                else: num <<= 1
                if num not in pos:
                    pos[num] = i
        # print(pos)
        ans = []
        for f, s in queries:
            n = f^s
            # print(f,s,n)
            p = pos.get(n)
            if p is None:
                ans.append((-1, -1))
            else:
                l = math.floor(math.log2(n)) if n else 0
                ans.append((p, p+l))
        
        return ans