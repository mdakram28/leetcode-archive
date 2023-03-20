from queue import Queue

_count = ''

def make_trie(words: List[str], root):
    for word in words:
        node = root
        for letter in word:
            node = node.setdefault(letter, {})
        if _count not in node:
            node[_count] = 1
        else:
            node[_count] += 1
    return root

def get_all_counts(root, k):
    q = [root]
    counts = []

    for node in q:
        # print(node)
        if _count in node and node[_count] > 0:
            counts.append(node[_count])
            if len(counts) == k:
                return counts
        for letter in node.keys():
            if len(letter) == 0:
                continue
            q.append(node[letter])
    return counts

def add_all_words(node, min_count, words, s=""):
    if _count in node and node[_count] >= min_count:
        words.append((min_count-node[_count], s))
    for letter in node.keys():
        if len(letter) == 0:
            continue
        add_all_words(node[letter], min_count, words, s+letter)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trie = make_trie(words, {})
        counts = get_all_counts(trie, k)
        counts.sort(reverse=True)
        min_count = counts[:k][-1]
        k_words = []
        add_all_words(trie, min_count, k_words)
        k_words.sort()
        # print(k_words)

        return list(map(lambda x: x[1], k_words[:k]))



