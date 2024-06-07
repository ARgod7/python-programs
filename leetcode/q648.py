# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

# Return the sentence after the replacement.

 

# Example 1:

# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# Example 2:

# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"


class Solution_0:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        s = set(dictionary)
        sentence = sentence.split()
        for j, w in enumerate(sentence):
            for i in range(1, len(w)):
                if w[:i] in s: 
                    sentence[j] = w[:i]
                    break
        return " ".join(sentence)

class Solution_1:
    def replaceWords(self, roots, sentence):
        rootset = set(roots)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))

class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        d = {w: len(w) for w in dictionary}
        mi, ma = min(d.values()), max(d.values())
        wrds = sentence.split()
        res = []
        for w in wrds:
            c = w
            for i in range(mi, min(ma, len(w)) + 1):
                ss = w[:i]
                if ss in d:
                    c = ss
                    break
            res.append(c)
        return " ".join(res)