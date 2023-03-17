class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        i = 0
        while i<len(word) and word[i] in node.children:
            node = node.children[word[i]]
            i+=1
        while i < len(word):
            new_node = TrieNode()
            node.children[word[i]] = new_node
            node = new_node
            i += 1
        node.end = True
        

    def search(self, word: str) -> bool:
        node = self.root
        i = 0
        while i<len(word) and word[i] in node.children:
            node = node.children[word[i]]
            i+=1
        return i == len(word) and node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        i = 0
        while i<len(prefix) and prefix[i] in node.children:
            node = node.children[prefix[i]]
            i+=1
        return i == len(prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)