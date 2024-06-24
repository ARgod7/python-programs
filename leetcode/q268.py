def missingNumber(nums: list[int]) -> int:
        max_num = max(nums)
        for i in range(max_num+1):
            if i not in nums:
                return i
        return 0

missingNumber([0,1])