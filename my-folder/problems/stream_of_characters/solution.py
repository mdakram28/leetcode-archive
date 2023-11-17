def make_trie(words):
    root = {}
    for word in words:
        node = root
        for c in word[::-1]:
            node = node.setdefault(c, {})
        node["$"] = True
    return root

def search_trie(root, word):
    node = root
    for c in word:
        if "$" in node:
            return True
        if c not in node:
            return False
        node = node[c]
    return "$" in node

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = make_trie(words)
        self.letters = deque()

    def query(self, letter: str) -> bool:
        self.letters.appendleft(letter)
        return search_trie(self.root, self.letters)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)