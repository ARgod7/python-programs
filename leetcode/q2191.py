def sortJumbled(mapping: list[int], nums: list[int]) -> list[int]:
        res = []
        for i , n in enumerate(nums):
            n = str(n)
            num = 0
            for c in n:
                num *= 10
                num += mapping[int(c)]
            res.append((num, i))
        res.sort()
        return [nums[p[1]] for p in res]