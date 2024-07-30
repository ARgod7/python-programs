def minimumDeletions(s: str) -> int:
        # res = 0
        # count_b = 0
        # for c in s:
        #     if c == 'a':
        #         res = min(res + 1, count_b)
        #     else:
        #         count_b += 1
        # return res
        res = 0
        count_b = 0
        for c in s:
            if c == 'b':
                count_b += 1
            elif count_b:
                res += 1
                count_b -= 1
        return res
        