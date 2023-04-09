
def make_trie(words):
    root = {}
    for i, word in enumerate(words):
        node = root
        for c in word:
            node = node.setdefault(c, {})
        node["_i"] = i
    return root

def get_all_matches(node, word, offset):
    i = offset
    while node and i < len(word) and word[i] in node:
        node = node[word[i]]
        i += 1
        if "_i" in node:
            yield node["_i"], i

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = make_trie(wordDict)
        idx = []
        sent = []

        def dfs(offset):
            if offset == len(s):
                sent.append(' '.join(wordDict[i] for i in idx))
                return
            for wi, next_offset in get_all_matches(root, s, offset):
                idx.append(wi)
                dfs(next_offset)
                idx.pop()
        
        dfs(0)
        return sent