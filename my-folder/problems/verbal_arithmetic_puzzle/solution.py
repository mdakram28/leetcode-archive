class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        letters = set(result)
        lastletters = set()
        for word in words:
            lastletters.add(word[0])
            letters.update(set(word))
        letters = sorted(list(letters))

        if any(len(w) > len(result) for w in words):
            return False

        # print(words, result)

        l2d = {}

        def check_assignment():
            left = sum(int(''.join(str(l2d[l]) for l in w)) for w in words)
            right = int(''.join(str(l2d[l]) for l in result))
            # if left == right:
            #     print([''.join(str(l2d[l]) for l in w) for w in words], ''.join(str(l2d[l]) for l in result))
            return left == right
            

        def select_options(i, carry):
            if len(l2d) == len(letters):
                valid = check_assignment()
                # print(l2d, "valid" if valid else "")
                return valid
            if i > len(result):
                return False

            to_select_for = list(set(w[-i] for w in words if i <= len(w) and w[-i] not in l2d))
            resletter = result[-i] if result[-i] not in l2d and result[-i] not in to_select_for else None

            rem = set(range(10)) - set(l2d.values())
            # print(i, rem, to_select_for, resletter)
            for selections in permutations(rem, len(to_select_for)):
                for l, d in zip(to_select_for, selections):
                    l2d[l] = d
                
                total = str(sum(l2d[w[-i]] for w in words if i <= len(w)) + carry)
                if resletter is not None:
                    if int(total[-1]) not in rem or int(total[-1]) in selections:
                        continue
                    l2d[resletter] = int(total[-1])
                
                # print([len(w)>1 and l2d[w[0]] == 0 for w in words if w[0] in l2d])

                if any(len(w)>1 and l2d[w[0]] == 0 for w in words if w[0] in l2d) or (len(result) > 1 and l2d.get(result[0], -1) == 0):
                    continue
                    
                # print(l2d)
                if int(total[-1]) != l2d[result[-i]]:
                    continue

                if select_options(i+1, int(total[:-1]) if len(total) > 1 else 0):
                    return True

            for l in to_select_for:
                del l2d[l]
            if resletter is not None and resletter in l2d:
                del l2d[resletter]

        
        return select_options(1, 0)
            
