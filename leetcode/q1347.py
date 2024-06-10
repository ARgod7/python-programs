from typing import Counter

def minSteps(s: str, t: str) -> int:
        smap = Counter(s)
        tmap = Counter(t)

        res = 0

        for i in tmap:
            if i in smap and tmap:
                res += abs(smap[i]-tmap[i])
        return res//2

minSteps(s="leetcode",t="practice")