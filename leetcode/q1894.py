def chalkReplacer(self, chalk: list[int], k: int) -> int:
        total = sum(chalk)
        k %= total
        for i, x in enumerate(chalk):
            k -= x
            if k < 0:
                return i