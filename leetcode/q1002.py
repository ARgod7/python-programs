# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]



from typing import Counter


def commonChars(self, words: list[str]) -> list[str]:
        count = Counter(words[0])

        for w in words:
            check = Counter(w)
            for c in count:
                count[c] = min(count[c],check[c])
        
        res = []
        for i in count.elements():
            res.append(i)
        return res
        