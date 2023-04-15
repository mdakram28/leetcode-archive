class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        l = len(beginWord)
        n = len(wordList)
        graph = collections.defaultdict(list)

        # for i, word in enumerate(wordList):
        #     idx[word] = i

        # if beginWord not in idx:
        #     idx[beginWord] = n
        #     n += 1
        #     wordList.append(beginWord)
        
        # letters = [set()]
        # for word in words:
        #     for i, letter in enumerate(word):
        #         letters[i].add(letter)


        for i, word1 in enumerate(wordList):
            for j, word2 in enumerate(wordList):
                if i==j: continue
                cnt = sum(1 if word1[pos] != word2[pos] else 0 for pos in range(l))
                if cnt == 1: graph[word1].append(word2)
        
        if beginWord not in graph:
            word1 = beginWord
            for j, word2 in enumerate(wordList):
                if i==j: continue
                cnt = sum(1 if word1[pos] != word2[pos] else 0 for pos in range(l))
                if cnt == 1:
                    graph[word1].append(word2)
                    graph[word2].append(word1)

        dist = collections.defaultdict(lambda: float('inf'))
        q = [(0, beginWord)]
        dist[beginWord] = 0

        
        while q:
            d, at = heapq.heappop(q)
            d += 1
            for to in graph[at]:
                if d < dist[to]:
                    dist[to] = d
                    heapq.heappush(q, (d, to))

        # print(dist, graph)
        if dist[endWord] == float('inf'):
            return []
        
        ret = []
        prev = []
        def add_all(at):
            # nonlocal startIdx
            prev.append(at)
            # print(prev)
            if dist[at] == 0:
                ret.append(list(reversed(prev)))
            else:
                for to in graph[at]:
                    if dist[to] == dist[at]-1:
                        add_all(to)

            prev.pop()

        add_all(endWord)

        return ret
        