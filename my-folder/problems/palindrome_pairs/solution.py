class Trie:
    def __init__(self, words):
        self.root = {}
        for i, word in enumerate(words):
            node = self.root
            for c in word:
                node = node.setdefault(c, {})
            node["_idx_"] = i
    
    def matches(self, word):
        node = self.root
        if "_idx_" in node:
            yield -1, node['_idx_']
        for i, c in enumerate(word):
            if c not in node:
                return None
            node = node[c]
            if "_idx_" in node:
                yield i, node['_idx_']
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie_fwd = Trie(words)
        trie_rev = Trie(map(reversed, words))
        ans = set()

        for i, word in enumerate(words):
            
            rev = word[::-1]
            for j, m in trie_fwd.matches(rev):
                if m == i: continue
                if rev[j+1:] == rev[j+1:][::-1]:
                    ans.add((m, i))
            
            for j, m in trie_rev.matches(word):
                if m == i: continue
                if word[j+1:] == word[j+1:][::-1]:
                    ans.add((i, m))
        
        return list(ans)





