from typing import Counter

def minSteps(s: str, t: str) -> int:
        s_map = Counter(s)
        t_map = Counter(t)
        res = 0
        for i in s_map:
            if s_map[i] > t_map[i]:
                res += abs(s_map[i] - t_map[i])
        return res