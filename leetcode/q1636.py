from collections import Counter


def frequencySort(self, nums: list[int]) -> list[int]:
        count = Counter(nums)
        nums.sort(key = lambda n: (count[n], -n))
        return nums
