class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = [words[0]]
        line_length = len(words[0])
        out = []
        spaces_all = " " * maxWidth
        line_with_spaces = []
        for word in words[1:]:
            if line_length + len(word) + 1 <= maxWidth:
                line.append(word)
                line_length += len(word) + 1
                continue
            num_spaces = len(line)-1 or 1
            letters = line_length - (len(line)-1)
            spaces = maxWidth - letters
            space_counts = [spaces//num_spaces] * num_spaces
            spaces -= (spaces//num_spaces) * num_spaces
            i = 0
            while spaces > 0:
                space_counts[i] += 1
                spaces -= 1
                i += 1
            space_counts.append(0)

            line_with_spaces.clear()
            i = 0
            for w in line:
                line_with_spaces.append(w)
                line_with_spaces.append(spaces_all[:space_counts[i]])
                i += 1
            
            out.append(''.join(line_with_spaces))

            line.clear()
            line.append(word)
            line_length = len(word)
        
        if len(line) > 0:
            line_with_spaces.clear()
            i = 0
            for w in line:
                line_with_spaces.append(w)
                if i < (len(line)-1):
                    line_with_spaces.append(" ")
                i += 1
            line_with_spaces.append(spaces_all[:maxWidth-(line_length)])
            out.append(''.join(line_with_spaces))

        return out