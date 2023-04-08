

def make_trie(words):
    root = {}
    for word in words:
        node = root
        for letter in word:
            node = node.setdefault(letter, {})
        node[""] = True
    return root


def prefix_matches(node, s):
    i = 0
    while i < len(s) and s[i] in node:
        node = node[s[i]]
        i += 1
        if node.get(""):
            yield i

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        root = make_trie(words)
        ret = []

        @cache
        def dfs(word, i):
            if i == len(word):
                return True
            elif i>len(word):
                return False
            for j in prefix_matches(root, word[i:]):
                if j == len(word):
                    continue
                if dfs(word, i+j):
                    return True
            return False

        for word in words:
            if dfs(word, 0):
                ret.append(word)
            
        return ret



