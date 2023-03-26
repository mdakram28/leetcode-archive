word_ind = "_ind"
word_found = "_found"
class Solution:
    def make_trie(self, words: List[str]):
        root = {}
        for i, word in enumerate(words):
            node = root
            for letter in word:
                node = node.setdefault(letter, {})
            node[word_ind] = i
        return root
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie_root = self.make_trie(words)
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        
        def search(r, c, node):
            if word_ind in node:
                node[word_found] = True
                # print(f"Found index = {node[word_ind]}")
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            elif visited[r][c]:
                return
            elif board[r][c] not in node:
                return

            visited[r][c] = True
            node = node[board[r][c]]
            search(r-1, c, node)
            search(r+1, c, node)
            search(r, c-1, node)
            search(r, c+1, node)
            visited[r][c] = False

        
        for r in range(m):
            for c in range(n):
                search(r, c, trie_root)
        
        found = []
        def add_all_words(node):
            if word_found in node:
                found.append(words[node[word_ind]])
            for child in node:
                if len(child) != 1:
                    continue
                add_all_words(node[child])
        
        add_all_words(trie_root)
        return found