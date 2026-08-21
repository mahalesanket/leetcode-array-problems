class Solution(object):
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):

            # Find words that can fit in this line
            line_words = []
            line_length = 0

            while i < len(words):
                word_length = len(words[i])

                # Minimum one space between words
                if line_length + word_length + len(line_words) > maxWidth:
                    break

                line_words.append(words[i])
                line_length += word_length
                i += 1

            # Last line OR line with only one word
            if i == len(words) or len(line_words) == 1:

                line = " ".join(line_words)

                # Add remaining spaces at the end
                line += " " * (maxWidth - len(line))

                result.append(line)

            else:
                # Fully justify the line

                total_spaces = maxWidth - line_length
                gaps = len(line_words) - 1

                # Minimum spaces per gap
                spaces = total_spaces // gaps

                # Extra spaces
                extra = total_spaces % gaps

                line = ""

                for j in range(gaps):

                    line += line_words[j]

                    # Left gaps get extra spaces
                    gap_spaces = spaces

                    if j < extra:
                        gap_spaces += 1

                    line += " " * gap_spaces

                # Add last word
                line += line_words[-1]

                result.append(line)

        return result