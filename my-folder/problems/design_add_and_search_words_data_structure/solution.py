
_end = ""

class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for letter in word:
            node = node.setdefault(letter, {})
        node[_end] = True

    def search(self, word: str) -> bool:
        l = len(word)
        q = [(0, self.root)]
        for i, node in q:
            if i == l:
                if _end in node:
                    return True
                else:
                    continue
            c = word[i]
            if c == '.':
                for letter, next_node in node.items():
                    if len(letter) == 0:
                        continue
                    q.append((i+1, next_node))
            elif c in node:
                q.append((i+1, node[c]))
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)