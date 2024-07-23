def sortPeople(names: list[str], heights: list[int]) -> list[str]:
        map = {}
        for h, n in zip(heights, names):
            map[h] = n
        res = []
        for h in reversed(sorted(heights)):
            res.append(map[h])
        return res
        