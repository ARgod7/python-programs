from typing import Counter


def minimumPushes(word: str) -> int:
        res = 0
        count = Counter(word)
        count = sorted(count.values(), reverse = True)
        res = sum(count[:8]) + 2*sum(count[8:16]) + 3*sum(count[16:24]) + 4*sum(count[24:26])
        return res

        