def singleNonDuplicate(nums: list[int]) -> int:
        l , r = 0, len(nums)-1
        while l <= r :
            m = l + ((r - l) // 2)
            if ((m - 1 < 0 or nums[m - 1] != nums[m]) and (m + 1 == len(nums) or nums[m] != nums[m + 1])):
                return nums[m]
            leftsize = m - 1 if nums[m - 1] == nums[m] else m
            if leftsize % 2:
                r = m - 1
            else:
                l = m + 1
singleNonDuplicate([1,1,2,2,3,3,4,8,8])
