from collections import defaultdict


def groupAnagrams(strs: list[str]) -> list[list[str]]:
        # res = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c)-ord("a")] += 1
        #     res[tuple(count)].append(s)
        # return res.values()
        res = defaultdict(list)

        for str in strs:
            key = ''.join(sorted(str))
            res[key].append(str)

        return res.values()
groupAnagrams(["eat","tea","tan","ate","nat","bat"])