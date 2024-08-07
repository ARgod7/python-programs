# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

 

# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

from collections import Counter, defaultdict


def frequencySort(s: str) -> str:
        # count = Counter(s)
        # m = max(count.values())
        # buc = defaultdict(list)
        # res = ""
        # for c, cnt in count.items():
        #     buc[cnt].append(c)
        # for i in range(m,0,-1):
        #       for c in buc[i]:
        #             res += c * i
        # return res
        count = Counter(s)
        res = ""
        for c,cnt in count.most_common():
            res += c*cnt
        return res
        
frequencySort('tree')
        
        