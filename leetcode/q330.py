def minPatches(nums: list[int], n: int) -> int:
        count = 0
        mx = 0
        for x in nums:
            while x > mx + 1:
                mx += mx + 1
                count += 1
                if mx >= n:
                     return count
            mx += x
            if mx >= n:
                return count
        while n > mx :
            mx += mx+1
            count += 1
        return count

minPatches([1,2,2,6,34,38,41,44,47,47,56,59,62,73,77,83,87,89,94],20)
        