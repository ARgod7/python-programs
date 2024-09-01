def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if len(original) != m*n:
            return []
        res = []
        for r in range(m):
            res.append(original[r*n:n*(r+1)])
        return res
        