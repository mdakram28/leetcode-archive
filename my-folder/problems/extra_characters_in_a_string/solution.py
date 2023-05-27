
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0 for i in range(len(s)+1)]
        
        def make_trie(words):
            root = {}
            for word in words:
                node = root
                for c in word:
                    node = node.setdefault(c, {})
                node["_END"] = True
            return root
        
        def iter_matches(i):
            node = root
            while i<n and node and s[i] in node:
                node = node[s[i]]
                i += 1
                if "_END" in node:
                    yield i
        
        root = make_trie(dictionary)
        
        for i in range(n-1, -1, -1):
            dp[i] = dp[i+1]+1
            for j in iter_matches(i):
                # print(i, j)
                dp[i] = min(dp[i], dp[j])
        # print(dp)
        return dp[0]
            
            